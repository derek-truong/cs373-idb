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
    });
    return (
      <table id="example" className="display table-responsive" cellSpacing="0" width="100%">
        <thead>
          <tr>
              <th>Name</th>
              <th>City</th>
              <th>Rating</th>
              <th>Number of Reviews</th>
              <th>Category  </th>
          </tr>
        </thead>
        <tbody>
        </tbody>
      </table>
    );
  }
});
ReactDOM.render(
  <AttractionTable url="/api/attractions" />,
  document.getElementById('content')
);