var AttractionTable = React.createClass({
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
    var attractionNodes = this.state.data.map(function(attraction) {
      addTableRow(attraction);
      return (
        <Attraction attr = {attraction}/>
      );
    });
    return (
      <table id="example" className="display" cellSpacing="0" width="100%">
        <thead>
          <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Rating</th>
              <th>City</th>
              <th>Number of Reviews</th>
              <th>Category</th>
          </tr>
        </thead>
        <tbody>
        </tbody>
      </table>
    );
  }
});
var Attraction = React.createClass({
  render: function() {
    return (
          <tr>
              <td data-search="0">{this.props.attr.id}</td>
              <td data-search="1">{this.props.attr.name}</td>
              <td data-search="2">{this.props.attr.rating}</td>
              <td data-search="3">{this.props.attr.city_id}</td>
              <td data-search="4">{this.props.attr.num_reviews}</td>
              <td data-search="5">{this.props.attr.category}</td>
          </tr>
    );
  }
});
ReactDOM.render(
  <AttractionTable url="/api/attractions" />,
  document.getElementById('content')
);