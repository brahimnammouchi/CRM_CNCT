// import Component from the react module
import React, { Component } from "react";
import Modal from "./Components/Modal";
import axios from 'axios'; 
// create a class that extends the component
class App extends Component {
    // add a constructor to take props
constructor(props) {
  super(props);
  this.state ={
    // the viewCompleted prop represents the status
    // of the task. Set it to false by default
    viewCompleted: false,
    activeItem:{
      client:"",
      datetime: "",
      completed: false
    },
    appelList: []
  };
}
//add compounent did mount
componentDidMount() {
  this.refreshList();
}
refreshList = () => {
  axios  //axios to send and receive HTTP request
  .get("http://localhost:8000/api/AppelTel/")
  .then(res => this.setState({appelList: res.data}))
  .catch(err => console.log(err));
};
//this arrow function takes status as a parameter
//and changes the status of viewCompleted to true
//if the status is true, else changes it to false
displayCompleted = status => {
  if (status) {
    return this.setState({viewCompleted:true});
  }
  return this.setState({viewCompleted:false});
};
//this array function renders two spans that help control
//the set of items to be displayed(ie, completed or incomplete)
renderTabList = () => {
  return (
    <div className="my-5 tab-list">
      <span
       onClick={() => this.displayCompleted(true)}
       className={this.state.viewCompleted ? "active" : ""}
       >
         completed
       </span>
       <span
       on onClick={() => this.displayCompleted(false)}
       className={this.state.viewCompleted ? "" : "active"}
       >
         incompleted
       </span>
    </div>
  );
};
//Main variable to render items on the screen
renderItems = () => {
  const {viewCompleted} =this.state;
  const newItems = this.state.appelList.filter(
    (item) => item.completed === viewCompleted
  );
  return newItems.map((item) => (
    <li
     key={item.id}
     className="List-group-item d-flex justify-content-between align-items-center"
    >
      <span
          className={`todo-title mr-2 ${
            this.state.viewCompleted ? "completed-todo" : ""
          }`}
      client={item.datetime}
      >
      {item.client}
      </span>
      <span>
      <button
            onClick={() => this.handleDelete(item)}
            className="btn btn-danger"
          >
            Delete
          </button>
        </span>
    </li>
  ));
};
toggle = () => {
  //add this after modal creation
  this.setState({ modal: !this.state.modal});
};
handleSubmit = (item) => {
  this.toggle();
  alert("save" + JSON.stringify(item));
};
//submit an item
 // Submit an item
 handleSubmit = (item) => {
  this.toggle();
  if (item.id) {
    // if old post to edit and submit
    axios
      .put("http://localhost:8000/api/AppelTel/${item.id}/", item)
      .then((res) => this.refreshList());
    return;
  }
  // if new post to submit
  axios
    .post("http://localhost:8000/api/AppelTel/", item)
    .then((res) => this.refreshList());
};
//delete item
handleDelete = (item) => {
  axios
  // eslint-disable-next-line no-template-curly-in-string
  .delete("http://localhost:8000/api/AppelTel/${item.id}/")
      .then((res) => this.refreshList());
};
// eslint-disable-next-line no-dupe-class-members
handleDelete = (item) => {
  alert("delete" + JSON.stringify(item));
};
// Create item
  createItem = () => {
    const item = { client: "", datetime: "", completed: false };
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
  //Edit item
  editItem = (item) => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
  // Start by visual effects to viewer
render () {
  return (
    <main className="content">
        <h1 className="text-success text-uppercase text-center my-4">
          Liste des Appel à faire
        </h1>
        <div className="row ">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="">
                <button onClick={this.createItem} className="btn btn-info">
                  Ajouter un appel
                </button>
              </div>
              {this.renderTabList()}
              <ul className="list-group list-group-flush">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
    </main>
  );
}
}
export default App;