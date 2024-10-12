>Name your Jupyter Notebook as:
>
>`TASK3_<your name>_<centre number>_<index number>.ipynb`


# Task 3

Write a program to format a description for a webpage into an HTML document.

The description for the program will be provided in a text file. Each element will be on a new line and will follow the structure:

<pre>HTML element: content</pre>

For example, in the text file `firstPage.txt` the first line is:

```
heading: My first page
```

The HTML element is 'heading' and the text for the heading is 'My first page'.

The HTML elements that can be included are in this table with an example and a description for the content.

| HTML Element | Example                                            | Description                                      |
|--------------|----------------------------------------------------|--------------------------------------------------|
| heading      | `heading: This is a title`                         | Formats the string `This is a title` with the h1 tag |
| subheading   | `subheading: This is a subtitle`                   | Formats the string `This is a subtitle` with the h2 tag |
| hyperlink    | `hyperlink: https://www.seab.gov.sg, Click`        | Formats the string `Click` as a hyperlink to `https://www.seab.gov.sg` |
| paragraph    | `paragraph: This is a paragraph`                   | Formats the string `This is a paragraph` as a paragraph |

All documents start and end with the HTML and body tags.

The data being used will not include any special characters. You will not be required to validate the content in each statement, for example, that a title is a valid title.

For each of the sub-tasks, add a comment statement at the beginning of the code, using the hash symbol `#`, to indicate the sub-task the program code belongs to, for example:

<pre>
# Task 3.1
Program code
</pre>

---

## Task 3.1

Write one function for each of the HTML elements `heading`, `subheading`, and `paragraph` to:
- take the text to format as a parameter
- format the text including HTML tags
- return the formatted text.

For example, if the text parameter for the heading function is `"My first page"`, the formatted text will be:

```
"<h1>My first page</h1>"
```
[1]

Test your program by calling the **three** functions with `"My element"` and outputting the return value from each.

[1]

---

## Task 3.2

Write a function for the HTML element `hyperlink` to:
- take the text to format as a parameter
- split the parameter into the URL and string
- format the text including HTML tags
- return the formatted text.

For example, if the text parameter is `"https://www.cambridge.org, Click here"`, the formatted text will be:

```
"<a href="https://www.cambridge.org">Click here</a>"
```

[1]

Test your program by calling the function with `"https://www.cambridgeinternational.org, Click here"` and outputting the return value.

[1]

---

## Task 3.3

The function `body()` takes a list as a parameter containing the text to convert into an HTML formatted document. Each element in the list has one HTML element for conversion.

Write the function to:
- call the appropriate function for each HTML element in the list
- create a single string containing all the formatted returned HTML elements
- insert the HTML and body opening and closing tags at the start and end of the string
- return either the complete formatted string, or `False` if there are any unrecognised elements.

[6]

---

## Task 3.4

The text file `firstPage.txt` contains the description of a web page that needs converting into an HTML document.

Write the function `read_data()`, to read in the data from a text file. The function needs to:
- take the name of a file (including extension) as input
- read each line from the file into a separate list element
- call the appropriate functions to convert the list to a formatted HTML string
- return the formatted HTML string.

Write the function `write_data()`, to store the formatted HTML string as an HTML file. The function needs to:
- take the name of a file (excluding extension) as input
- take the formatted HTML string to write as input
- insert the string `<!DOCTYPE html>` at the start of the file
- write the formatted string to the file with the name input and the extension `".html"`.

Output an appropriate message if the data cannot be converted into HTML.

Call the function `read_data()` then call the function `write_data()`.

[9]

Run your program **two** times with the following inputs:

### Test 1:
- `firstPage.txt`
- `test`

### Test 2:
- `website.txt`
- `theWebsite`

[3]

Save your Jupyter Notebook for Task 3.
