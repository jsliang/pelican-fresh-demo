title: Codes Demo
Creator: jsliang
date: 2013-02-17 02:11:53
category: Programming
tags: Pelican, theme, programming
slug: codes-demo

Hello World program sources from [Wikipedia: List of Hello world program examples](http://en.wikipedia.org/wiki/List_of_Hello_world_program_examples).

# [Ada](http://en.wikipedia.org/wiki/Ada_(programming_language))
```
with Ada.Text_IO;

procedure Hello_World is
 use Ada.Text_IO;
begin
    Put_Line("Hello, world!");
end;
```

# [C](http://en.wikipedia.org/wiki/C_(programming_language))
```C
#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("Hello, world!\n");

    return 0;
}
```

# [C++](http://en.wikipedia.org/wiki/C%2B%2B)
```C++
#include <iostream>
using namespace std;
int main()
{
    cout << "Hello, world!" << endl;
    return 0;
}
```

# [HTML](http://en.wikipedia.org/wiki/HTML)
```HTML
<!DOCTYPE html>
<html>
<body>
Hello, world!
</body>
</html>
```

# [Java](http://en.wikipedia.org/wiki/Java_(programming_language))
```Java
public class HelloWorld {
   public static void main(String[] args) {
       System.out.println("Hello, world!");
   }
}
```

# [JavaScript](http://en.wikipedia.org/wiki/JavaScript)

To write to an HTML document:
```
document.write("Hello, world!");
```

To display an alert dialog box:
```
alert("Hello, world!");
```


To write to a console/debugging log:
```
console.log("Hello, world!");
```


Using Mozilla's Rhino:
```
print("Hello, world!");
```


Using Windows Script Host:
```
WScript.Echo("Hello, world!");
```

# [Python](http://python.org/)
Python 2
```python
print "Hello, world!"
```

Python 3
```python
print("Hello, world!")
```

# [Ruby](http://www.ruby-lang.org/)
```Ruby
puts "Hello, world!"
```

# [Shell](http://en.wikipedia.org/wiki/Bourne_shell)
```shell
echo "Hello, world!"
```

# [SQL](http://en.wikipedia.org/wiki/SQL)
```SQL
SELECT "Hello, world!" FROM DUMMY; -- DUMMY is a standard table in SAP HANA.
SELECT "Hello, world!" FROM DUAL; -- DUAL is a standard table in Oracle.
SELECT "Hello, world!" -- This will work in SQL Server.
```

