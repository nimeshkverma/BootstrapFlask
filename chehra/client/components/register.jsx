import React from 'react';
import { Link } from 'react-router';

export default class Register extends React.Component {
	constructor(props) {
		super(props);
	}
	render() {
		return (
			<div id="login-overlay" className="modal-dialog">
				<div className="modal-content">
					<div className="modal-header">
						<h4 className="modal-title" id="myModalLabel">Register with ReactFlask Boilerplate</h4>
					</div>
					<div className="modal-body">
						<form id="registerForm" method="POST" >
							<div className="form-group">
								<div className="col-xs-6">
									<label htmlFor="InputName">First Name</label>
									<div className="input-group">
										<input type="text" className="form-control" name="first_name" placeholder="Enter First Name" required />
										<span className="input-group-addon"><span className="glyphicon glyphicon-asterisk"></span></span>
									</div>
									<br/>
									<label htmlFor="InputName">Username</label>
									<div className="input-group">
										<input type="text" className="form-control" name="username" placeholder="Enter Username" required />
										<span className="input-group-addon"><span className="glyphicon glyphicon-asterisk"></span></span>
									</div>
									<hr/>
								</div>
							</div>
							<div className="form-group">
								<div className="col-xs-6">
									<label htmlFor="InputName">Last Name</label>
									<div className="input-group">
										<input type="text" className="form-control" name="last_name" placeholder="Enter Last Name" required />
										<span className="input-group-addon"><span className="glyphicon glyphicon-asterisk"></span></span>
									</div>
									<br/>
									<label htmlFor="InputPassword">Enter Password</label>
									<div className="input-group">
										<input type="password" className="form-control" name="password" placeholder="Enter Password" required />
										<span className="input-group-addon"><span className="glyphicon glyphicon-asterisk"></span></span>
									</div>
									<hr/>
								</div>
							</div>

							<div className="form-group">
								<div className="col-xs-12">
									<label htmlFor="InputEmail">Enter Email</label>
									<div className="input-group">
										<input type="email" className="form-control" name="email" placeholder="Enter Email" required />
										<span className="input-group-addon"><span className="glyphicon glyphicon-asterisk"></span></span>
									</div>
									<br/>
								</div>
							</div>

						<div className="form-group">
							<div className="col-xs-12">
								<input type="submit" name="submit" id="submit" value="Register" className="btn btn-success" />
							</div>
							<p>Already a member? Please <Link to="login">Login</Link> </p>
						</div>
					</form>
				</div>
			</div>
		</div>
		)
	}
}
