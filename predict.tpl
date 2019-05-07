<html>
  <head>
    <title>Задачи на день</title>
  </head>
  <body>
  <h1>Текущие задачи</h1>
  <ul id="todo-list"></ul>
  % for task in tasks:
    <li>
      <input class='checkbox' type='checkbox' />
      {{ task }}
      <a class="remove" href="#">X</a>
      <hr/>
    </li>
  % end
  <br/>
  <form id="todo-add">
    <input type="text" class="form-control"/>
    <button class="add" type="submit">+</button>
  </form>
  </body>

</html>