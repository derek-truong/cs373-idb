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
          image_uri = {recipe.image_uri} ready_in_minutes = {recipe.ready_in_minutes}>
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
          showModal: false
      };
  },
  close(){
    this.setState({
      showModal: false
    });
  },
  open(){
    this.setState({
      showModal: true
    });
  },
  render: function() {
    var Modal = ReactBootstrap.Modal;
    var Button  = ReactBootstrap.Button;
    var showModal = this.state.showModal;
    return (

      <div className="recipe">
        <li><a onClick={this.open}>{this.props.title}</a></li>

        <Modal show={this.state.showModal} onHide={this.close}>
          <Modal.Header closeButton>
              <Modal.Title>{this.props.title}</Modal.Title>
          </Modal.Header>

          <Modal.Body>
            <img src = {this.props.image_uri} />
            <div class="recipeInfo">
              <h4>Cuisine:</h4>
              <p>{this.props.cuisine}</p>
            </div>

            <div class="recipeInfo">
              <h4>Time in Minutes to Cook:</h4>
              <p>{this.props.ready_in_minutes}</p>
            </div>
          </Modal.Body>
          <Modal.Footer>
            <Button bsStyle="info" onClick={this.close}>Close</Button>
          </Modal.Footer>
        </Modal>
      </div>
    );
  }
});

ReactDOM.render(
  <MenuBox url="/api/recipes?page=" />,
  document.getElementById('menuList')
);