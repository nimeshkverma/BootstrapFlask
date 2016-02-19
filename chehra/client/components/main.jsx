import React from 'react';
import { Router, Route, Link, browserHistory } from 'react-router';
import Header from './header';

export default class Main extends React.Component {
	constructor(props) {
		super(props);
	}
	render() {
		return (
			<div>
				<Header />
				{this.props.children}
			</div>
		)
	}
}
