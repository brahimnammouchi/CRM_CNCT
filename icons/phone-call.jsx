import React from 'react';

function PhoneCall(props) {
	const fill = props.fill || 'currentColor';
	const secondaryfill = props.secondaryfill || fill;
	const title = props.title || "phone call";

	return (
		<svg height="48" width="48" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
	<title>{title}</title>
	<g>
		<path d="M46,21a1,1,0,0,1-1-1A17.018,17.018,0,0,0,28,3a1,1,0,0,1,0-2A19.021,19.021,0,0,1,47,20,1,1,0,0,1,46,21Z" fill="#49c549"/>
		<path d="M38,21a1,1,0,0,1-1-1,9.011,9.011,0,0,0-9-9,1,1,0,0,1,0-2A11.013,11.013,0,0,1,39,20,1,1,0,0,1,38,21Z" fill="#9ee09e"/>
		<path d="M31.376,29.175,27.79,33.658A37.835,37.835,0,0,1,14.343,20.212l4.483-3.586a3.047,3.047,0,0,0,.88-3.614l-4.087-9.2A3.045,3.045,0,0,0,12.068,2.1L4.29,4.115A3.066,3.066,0,0,0,2.029,7.5,45.2,45.2,0,0,0,40.5,45.971a3.062,3.062,0,0,0,3.383-2.26L45.9,35.932a3.047,3.047,0,0,0-1.712-3.551L34.99,28.3A3.046,3.046,0,0,0,31.376,29.175Z" fill="#3d6c7b"/>
	</g>
</svg>
	);
};

export default PhoneCall;