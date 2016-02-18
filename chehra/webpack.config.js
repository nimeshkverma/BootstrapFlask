var webpack = require('webpack');
var path = require('path');

module.exports = {
	context: __dirname + '/client',
	entry: [
		'./router'
	],
	output: {
		path: __dirname + '/build/',
		filename: 'bundle.js',
	},
	debug: true,
	devtool: "#inline-source-map",
	resolve: {
		extensions: ['', '.jsx','.js']
	},
	module: {
		loaders: [{
			test: /\.jsx?$/,
			loaders: ['babel'],
			exclude: /node_modules/
		}]
	},
};
