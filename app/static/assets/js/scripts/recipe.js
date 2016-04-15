var data = [
        {id: 1, title: "Pete Hunt", text: "This is one comment"},
        {id: 3, title: "Pete Hunt", text: "This is one comment"},
        {id: 4, title: "Pete Hunt", text: "This is one comment"},
        {id: 5, title: "Pete Hunt", text: "This is one comment"},
        {id: 6, title: "Pete Hunt", text: "This is one comment"},
        {id: 7, title: "Pete Hunt", text: "This is one comment"},
        {id: 8, title: "Pete Hunt", text: "This is one comment"},
        {id: 9, title: "Pete Hunt", text: "This is one comment"},
        {id: 10, title: "Pete Hunt", text: "This is one comment"},
        {id: 11, title: "Pete Hunt", text: "This is one comment"},
        {id: 12, title: "Pete Hunt", text: "This is one comment"},
        {id: 13, title: "Pete Hunt", text: "This is one comment"},
        {id: 14, title: "Pete Hunt", text: "This is one comment"},
        {id: 2, title: "Jordan Walke", text: "This is *another* comment"}
      ];

var MenuBox = React.createClass({
  render: function() {
    return (
      <div className="menuBox">
        <RecipeList data={this.props.data} />
      </div>
    );
  }
});

var RecipeList = React.createClass({
  render: function() {
    var recipeNodes = this.props.data.map(function(recipe) {
      return (
        <Recipe title={recipe.title} key={recipe.id}>
          {recipe.text}
        </Recipe>
      );
    });
    return (
      <div className="recipeList">
        <ul>{recipeNodes}</ul>
      </div>
    );
  }
});

var Recipe = React.createClass({
  render: function() {
    return (
      <div className="recipe">
        
        <li>{this.props.title}</li>
      </div>
    );
  }
});

ReactDOM.render(
  <MenuBox data={data} />,
  document.getElementById('menuList')
);