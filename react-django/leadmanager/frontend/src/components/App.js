import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';

import Header from './layout/Header';
import Dashboard from './leads/Dashboard';

class App extends React.Component { // Our component
    render() {
        return (
            <Fragment>
                <Header />
                <div className="container">
                    <Dashboard />
                </div>
            </Fragment>

        )
    }
}

// ReactDOM inserts our main App component into an element with the ID of 'app'
// which is in templates/frontend/index.html
ReactDOM.render(<App />, document.getElementById('app'));