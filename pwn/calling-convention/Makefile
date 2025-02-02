include ctf_tool.mk

CFLAGS += -fno-stack-protector -no-pie -z norelro
name = calling_convention

ALL = challenge.zip $(name) flag.txt
all: $(ALL)
clean:
	rm -rf $(ALL)

challenge.zip: $(name)

flag.txt: .dynamic_flag
flag.txt: FLAG_TEXT = R0p_Ch41ns
