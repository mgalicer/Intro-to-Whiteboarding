"tr" stands for translate or transliterate, and is a common shell program that replaces or removes specific characters in a data set.

You can try it out in your command line:

```
tr abc ABC <<< bananas
#=> BAnAnAs
```

Write a method that implements tr. The method should take three string arguments: from, to, and str (the output). Built-in string methods are not allowed!

Examples:
```
tr("old", "123", "hello") => he221
tr("abc", "lol", "SEXTON") => SEXTON
tr("moo", "oom", "moomoo") => ommomm
```

Extra cred: Did you modify the original string, or create a new one? Try implementing the opposite.