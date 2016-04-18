// var data = [recipes: {"image_uri": "https://spoonacular.com/recipeImages/African-Bean-Soup-632003.jpg", 
//     "servings": 4, "ready_in_minutes": 45, "cuisine": "african", "id": 1, "title": "African Bean Soup"}, 
//     {"image_uri": "https://spoonacular.com/recipeImages/Ethiopian-Lentil-Curry-642468.jpg", 
//     "servings": 6, "ready_in_minutes": 75, "cuisine": "african", "id": 2, "title": "Ethiopian Lentil Curry"}, 
//   {"image_uri": "https://spoonacular.com/recipeImages/North-African-Chickpea-Soup-653275.jpg", 
//     "servings": 4, "ready_in_minutes": 45, "cuisine": "african", "id": 3, "title": "North African Chickpea Soup"}
//     ];

var MenuBox = React.createClass({
  getInitialState: function() {
    return {data: []};
  },
  loadDataFromServer: function() {
    var recipeData = [];
    for (var i = 1; i < 40; i++) {
      $.ajax({
        url: this.props.url + i,
        dataType: 'json',
        cache: false,
        // async: false,
        success: function(data) {
          for (var j = 0, len=data.length; j <len; j++){
            recipeData.push(data[j]);
          }
          this.setState({data: recipeData});
        }.bind(this),
        error: function(xhr, status, err) {
          // console.error(this.props.url, status, err.toString());
        }.bind(this)
      });
    }
  },
  componentDidMount: function() {
    this.loadDataFromServer();
  },
  render: function() {
    return (
      <div className="menuBox">
        <RecipeList data={this.state.data} />
      </div>
    );
  }
});

var RecipeList = React.createClass({
  render: function() {
    var recipeNodes = this.props.data.map(function(recipe) {
      return (
        <Recipe title={recipe.title} key={recipe.id} cuisine = {recipe.cuisine}
          image_uri = {recipe.image_uri} >
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
  getInitialState: function() {
      return {
          isSelected: false
      };
  },
  handleClick: function() {
    if(this.state.isSelected){
      this.setState({
        isSelected: false
      })
    }else{
      this.setState({
        isSelected: true
      })
    }

  },
  render: function() {
    var isSelected = this.state.isSelected;
    return (
      <div className="recipe">
        <li><a onClick={this.handleClick}>{this.props.title}</a></li>
        {this.state.isSelected ? <RecipeImg image = {this.props.image_uri}></RecipeImg> : null}
      </div>
    );
  }
});

var RecipeImg = React.createClass({
  render: function(){
    console.log(this.props.image);
    return (
      <div className = "recipeImg">
        <img src = {this.props.image} />
      </div>
    );
  }
})

ReactDOM.render(
  <MenuBox url="/api/recipes?page=" />,
  document.getElementById('menuList')
);