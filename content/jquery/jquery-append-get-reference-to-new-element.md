Title: Get reference to new element added with jQuery.append()
Date: 2016-02-13 18:53
Category: jQuery
Tags: jquery, javascript, html

First, create new element and save reference to object:

```javascript
var board = $('<div class="chess-board"></div>');
```

Then, add new object to DOM via `appendTo()`` routine:

```javascript
var board.appendTo('#container');
```

or, if you already have reference to container, use that instead of selector:

```javascript
var container = $('#container');
var board.appendTo(container);
```
