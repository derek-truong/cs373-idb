var RestaurantTable = React.createClass({
  loadDataFromServer: function() {
    // $.get(this.props.url, function(result) {
    //   if (this.isMounted()) {
    //     this.setState({data: data})
    //   }
    // }.bind(this))
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
    this.loadDataFromServer();
  },
  componentDidMount: function() {
    // initMyDataTable();
    // $('#example').dataTable().fnDraw();
    $('#example').dataTable().fnDraw();

  },
  componentDidUpdate: function(){
    // $('#example').dataTable().fnDrawCallBack();
    // $('#example').dataTable().ajax.reload( function ( json ) {
    //   $('#sort').val( json.lastInput );
    // })
  },

  // componentDidUpdate: function(){
  //   $('#example').dataTable({
  //     "sPaginationType": "bootstrap",
  //     "bAutoWidth": false,
  //     "bDestroy": true, 
  //   });
  // },
  componentWillUnmount: function() {
    $('#example').dataTable().clearInterval();
  },
  render: function() {
    var restaurantNodes = this.state.data.map(function(restaurant) {
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
            {restaurantNodes}
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
              <td data-search="0">{this.props.rest.name}</td>
              <td data-search="0">{this.props.rest.location}</td>
              <td data-search="0">{this.props.rest.rating}</td>
              <td data-search="0">{this.props.rest.category}</td>
              <td data-search="0">{this.props.rest.address}</td>
          </tr>
    );
  }
});

ReactDOM.render(
  <RestaurantTable url="/api/restaurants" />,
  document.getElementById('content')
);