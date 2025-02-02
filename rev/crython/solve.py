import ast
import sys
import re
file = open("crython.py", "r")
data = file.read()
tree = ast.parse(data)
jumbled_bits = 14154190239817593391562602231552196407925674789718962804833972736086242830332675315723974651
print(tree)
sys.setrecursionlimit(900000)
class ReplaceConstantOps(ast.NodeTransformer):

    def visit_BinOp(self, node):
        try:
            o = node.op
            # print(l, o, r)
            node.left = self.visit(node.left)
            node.right = self.visit(node.right)
            l = node.left
            r = node.right
            if type(l) != ast.Constant or type(r) != ast.Constant:
                return node
            if type(o) == ast.BitAnd:
                return ast.Constant(l.value & r.value)
            elif type(o) == ast.BitOr:
                return ast.Constant(l.value | r.value)
            elif type(o) == ast.BitXor:
                return ast.Constant(l.value ^ r.value)
            elif type(o) == ast.Add:
                return ast.Constant(l.value + r.value)
            elif type(o) == ast.Sub:
                return ast.Constant(l.value - r.value)
            elif type(o) == ast.RShift:
                return ast.Constant(l.value >> r.value)
            elif type(o) == ast.LShift:
                return ast.Constant(l.value << r.value)
            elif type(o) == ast.Pow:
                return ast.Constant(l.value ** r.value)
            elif type(o) == ast.Mult:
                return ast.Constant(l.value * r.value)
            else:
                print(type(o))
                return ast.BinOp(l, node.op, r)
        except Exception as e:
            print(e)
            return node
    def visit_UnaryOp(self, node):
        try:
            o = node.op
            node.operand = self.visit(node.operand)
            v = node.operand
            if type(v) != ast.Constant:
                return node
            if type(o) == ast.Invert:
                return ast.Constant(~v.value)
            elif type(o) == ast.Not:
                return ast.Constant(not v.value)
            elif type(o) == ast.UAdd:
                return ast.Constant(+v.value)
            elif type(o) == ast.USub:
                return ast.Constant(-v.value)
            else:
                return ast.UnaryOp(node.op, v)
        except Exception as e:
            print(e)
            return node
  
    def visit_Call(self, node):
        try:
            name = node.func.id
            args = tuple()
            if name == "sum":
                for arg in range(0, len(node.args)):    
                    if type(node.args[arg]) == ast.Tuple:
                        for elt in range(0, len(node.args[arg].elts)):
                            node.args[arg].elts[elt] = self.visit(node.args[arg].elts[elt])
                            args += (node.args[arg].elts[elt].value,)
                    else:
                        node.args[arg] = self.visit(node.args[arg])
                        args += (node.args[arg].value,)
                return ast.Constant(sum(args))
            else:
                return node
        except Exception as e:
            print(e)
            return node

transformer = ReplaceConstantOps()
new_tree = transformer.visit(tree)
lol = ast.unparse(new_tree)
bit_regex = r"\(f & ([0-9]+)\) ([<>]+) ([0-9]+)"
instances = re.findall(bit_regex, lol)
final = 0
print(lol)
for i in instances:
    num = eval(" ".join(i)) & jumbled_bits
    if num:
        final |= int(i[0])
print(final.to_bytes(50, 'big'))