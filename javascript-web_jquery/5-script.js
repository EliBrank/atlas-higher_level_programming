$(document).ready(function () {
  $('#add_item').click(function () {
    const listItem = '<li>Item</li>';
    $('.my_list').append(listItem);
  });
});
