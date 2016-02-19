import React from 'react';
import { Link } from 'react-router';

let style = {
	lineHeight: 2
};

export default class Login extends React.Component {
	constructor(props) {
		super(props);
	}
	render() {
		return (
			<div id="login-overlay" className="modal-dialog">
				<div className="modal-content">
					<div className="modal-header">
						<h4 className="modal-title" id="myModalLabel">Login to <b>FlaskReact Boilerplate</b></h4>
					</div>
					<div className="modal-body">
						<div className="row">
							<div className="col-xs-6">
								<div className="well">
									<form id="loginForm" method="POST">
										<div className="form-group">
											<label htmlFor="username" className="control-label">Username</label>
											<input type="text" className="form-control" name="username" value="" required="" title="Please enter your username" placeholder="username" />
											<span className="help-block"></span>
										</div>
										<div className="form-group">
											<label htmlFor="password" className="control-label">Password</label>
											<input type="password" className="form-control" name="password" placeholder="password" value="" required="" title="Please enter your password" />
											<span className="help-block"></span>
										</div>
										<div id="loginErrorMsg" className="alert alert-error hide">Wrong username or password</div>
										<div className="checkbox">
											<label>
												<input type="checkbox" name="remember" id="remember" /> Remember login
											</label>
											<p className="help-block">(if this is a private computer)</p>
										</div>
										<button type="submit" value="login" name="submit" className="btn btn-success btn-block">Login</button>
									</form>
								</div>
							</div>
							<div className="col-xs-6">
								<p className="lead">Register now for <span className="text-success">FREE</span></p>
									<ul className="list-unstyled" style={style}>
										<li><span className="fa fa-check text-success"></span> React Flask Boilerplate</li>
										<li><span className="fa fa-check text-success"></span> React Flask Boilerplate</li>
										<li><span className="fa fa-check text-success"></span> React Flask Boilerplate</li>
										<li><span className="fa fa-check text-success"></span> React Flask Boilerplate</li>
										<li><span className="fa fa-check text-success"></span> React Flask Boilerplate</li>
										<li><span className="fa fa-check text-success"></span> React Flask Boilerplate</li>
									</ul>
								<Link to="register" className="btn btn-info btn-block">Yes please, register now!</Link>
							</div>
						</div>
					</div>
				</div>
			</div>
		)
	}
}
