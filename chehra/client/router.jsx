import React from 'react';
import { render } from 'react-dom';
import Main from './components/main';
import Login from './components/login';
import Register from './components/register';
import { Router, Route, Link, browserHistory } from 'react-router';

render((
	<Router history={browserHistory}>
		<Route path="/" component={Main}>
			<Route path="/login" component={Login}/>
			<Route path="/register" component={Register}/>
		</Route>
	</Router>
), document.getElementById('root'));
