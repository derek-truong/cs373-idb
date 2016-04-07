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
      return (
        <City ct = {city}/>
      );
    });
    return (
      <table id="example" className="display" cellSpacing="0" width="100%">
        <thead>
          <tr>
              <th>ID</th>
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
var City = React.createClass({
  render: function() {
    return (
          <tr>
              <td data-search="0">{this.props.ct.id}</td>
              <td data-search="1">{this.props.ct.name}</td>
              <td data-search="2">{this.props.ct.population}</td>
              <td data-search="3">{this.props.ct.country}</td>
              <td data-search="4">{this.props.ct.demonym}</td>
              <td data-search="5">{this.props.ct.elevation}</td>
          </tr>
    );
  }
});
ReactDOM.render(
  <CityTable url="/api/cities" />,
  document.getElementById('content')
);