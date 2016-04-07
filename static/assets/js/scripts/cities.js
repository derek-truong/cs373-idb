var CityTable = React.createClass({
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
    var cityNodes = this.state.data.map(function(city) {
      addTableRow(city);
    });
    return (
      <table id="example" className="display" cellSpacing="0" width="100%">
        <thead>
          <tr>
              <th>Name</th>
              <th>Population</th>
              <th>Country</th>
              <th>Demonym</th>
              <th>Elevation</th>
          </tr>
        </thead>
        <tbody>
        </tbody>
      </table>
    );
  }
});

ReactDOM.render(
  <CityTable url="/api/cities" />,
  document.getElementById('content')
);