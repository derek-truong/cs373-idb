var data = [
//   {id: 25, name: "Pete Hunt", rating: "1", location:1, num_reviews:5 , category: "This is one restaurant", address:"Coolio"},
//   {id: 50, name: "McDonalds", rating: "2", location:3, num_reviews:8 , category: "Anoda One", address:"Coolioerrersfj"}
];
var RestaurantTable = React.createClass({
  loadDataFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      success: function(data) {

        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  getInitialState: function() {
    return {data: []};
  },
  componentWillMount: function() {
    initMyDataTable();
    this.loadDataFromServer();
  },
  componentDidMount: function() {
    initMyDataTable();
  },
  render: function() {
    // var restaurantNodes = this.props.data.map(function(restaurant) {
    var restaurantNodes = this.state.data.map(function(restaurant) {
      addTableRow(restaurant);
      return (
        <Restaurant rest = {restaurant}/>
      );
    });
    return (
      <table id="example" className="display" cellSpacing="0" width="100%">
        <thead>
          <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Location</th>
              <th>Rating</th>
              <th>Category</th>
              <th>Address</th>
          </tr>
        </thead>
        <tbody>
        </tbody>
      </table>
    );
  }
});
var Restaurant = React.createClass({
  render: function() {
    return (
          <tr>
              <td data-search="0">{this.props.rest.id}</td>
              <td data-search="1">{this.props.rest.name}</td>
              <td data-search="2">{this.props.rest.location}</td>
              <td data-search="3">{this.props.rest.rating}</td>
              <td data-search="4">{this.props.rest.category}</td>
              <td data-search="5">{this.props.rest.address}</td>
          </tr>
    );
  }
});
ReactDOM.render(
  <RestaurantTable url="/api/restaurants" />,
  document.getElementById('content')
);