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
    });
    return (
      <table id="example" className="display" cellSpacing="0" width="100%">
        <thead>
          <tr>
              <th>Name</th>
              <th>City</th>
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

ReactDOM.render(
  <RestaurantTable url="/api/restaurants" />,
  document.getElementById('content')
);