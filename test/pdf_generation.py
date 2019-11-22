import pdfkit 
options = {'print-media-type': None, 'background': None, 'images': None, 'quiet': None, 'encoding': 'UTF-8', 'margin-right': '15mm', 'margin-left': '15mm', 'margin-top': '15mm', 'margin-bottom': '15mm', 'cookie': [('sid', 'b9aa3ae87da55955c3b679d553db07eb81e2a1760ebb682599ab9196')], 'page-size': 'A4', 'disable-javascript': '', 'disable-local-file-access': '', 'disable-smart-shrinking': 'true'}
html = """<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>
   LR-00104
  </title>
  <meta content="frappe" name="generator"/>
  <link href="https://gamma-velocity.elasticrun.in/assets/frappe/css/bootstrap.css" rel="stylesheet" type="text/css"/>
  <link href="https://gamma-velocity.elasticrun.in/assets/frappe/css/font-awesome.css" rel="stylesheet" type="text/css"/>
  <style>
   @media screen {
	.print-format-gutter {
		background-color: #ddd;
		padding: 15px 0px;
	}
	.print-format {
		background-color: white;
		box-shadow: 0px 0px 9px rgba(0,0,0,0.5);
		max-width: 8.3in;
		min-height: 11.69in;
		padding: 0.75in;
	    margin: auto;
	}

	.print-format.landscape {
		max-width: 11.69in;
		padding: 0.2in;
	}

	.page-break {
		padding: 30px 0px;
		border-bottom: 1px dashed #888;
	}

	.page-break:first-child {
		padding-top: 0px;
	}

	.page-break:last-child {
		border-bottom: 0px;
	}

	/* mozilla hack for images in table */
	body:last-child .print-format td img {
		width: 100% !important;
	}

	@media(max-width: 767px) {
		.print-format {
			padding: 0.2in;
		}
	}
}

@media print {
	.print-format p {
		margin-left: 1px;
		margin-right: 1px;
	}
}

.data-field {
	margin-top: 5px;
	margin-bottom: 5px;
}

.data-field .value {
	word-wrap: break-word;
}

.important .value {
	font-size: 120%;
	font-weight: bold;
}

.important label {
	line-height: 1.8;
	margin: 0px;
}

.table {
	margin: 20px 0px;
}

.square-image {
	width: 100%;
	height: 0;
	padding: 50% 0;
	background-size: contain;
	/*background-size: cover;*/
	background-repeat: no-repeat !important;
	background-position: center center;
	border-radius: 4px;
}

.print-item-image {
	object-fit: contain;
}

.pdf-variables,
.pdf-variable,
.visible-pdf {
	display: none !important;
}

.print-format {
	font-size: 9pt;
	font-family: "Helvetica Neue", Helvetica, Arial, "Open Sans", sans-serif;
	-webkit-print-color-adjust:exact;
}

.page-break {
	page-break-after: always;
}

.print-heading {
	border-bottom: 1px solid #aaa;
	margin-bottom: 10px;
}

.print-heading h2 {
	margin: 0px;
}
.print-heading h4 {
	margin-top: 5px;
}

table.no-border, table.no-border td {
	border: 0px;
}

.print-format label {
	/* wkhtmltopdf breaks label into multiple lines when it is inline-block */
	display: block;
}

.print-format img {
	max-width: 100%;
}

.print-format table td > .primary:first-child {
	font-weight: bold;
}

.print-format td, .print-format th {
	vertical-align: top !important;
	padding: 6px !important;
}

.print-format p {
	margin: 3px 0px 3px;
}

table td div {
	
	/* needed to avoid partial cutting of text between page break in wkhtmltopdf */
	page-break-inside: avoid !important;
	
}

/* hack for webkit specific browser */
@media (-webkit-min-device-pixel-ratio:0) {
	thead, tfoot {
		display: table-header-group;
	}
}

[document-status] {
	margin-bottom: 5mm;
}

.signature-img {
	background: #fff;
	border-radius: 3px;
	margin-top: 5px;
	max-height: 150px;
}

.print-heading {
	text-align: right;
	text-transform: uppercase;
	color: #666;
	padding-bottom: 20px;
	margin-bottom: 20px;
	border-bottom: 1px solid #d1d8dd;
}

.print-heading h2 {
	font-size: 24px;
}

.print-format th {
	background-color: #eee !important;
	border-bottom: 0px !important;
}

/* modern format: for-test */

.section-break { padding: 5px 5px 5px 5px; border-bottom: 1px solid #eee; }
  .page-break { display:block; clear:both; page-break-after: always;!important}

#podbox{
    margin-top: 20px!important;
}
#background{
    margin-top: 50px!important;
    position: absolute!important;
}


.background-class{
height:900px!important;
}
  </style>
 </head>
 <body>
  <div class="print-format-gutter">
   <div class="print-format">
    <style>
     @page {	
		@top-center {
			content: element(pageHeader);
		}
	
		@bottom-left {
			content: element(pageFooter);
		}
	}
	#pageHeader{
		position: running(pageHeader);
	}
	
	#pageFooter{
		position: running(pageFooter) !important;
	}
	#print-format td, .print-format th {
		vertical-align: top !important;
		 padding: 5px !important; 
		 padding-right: 0px !important;
		 background-color: white !important;
	}
	
	#podbox-inner td{
		border: 1px solid black !important;
		text-align: left !important;
	}
	.bg-top-class{
	    height: 310px!important;
	}
	.background-class{
	height:800px!important;
	}
	.empty-background-class{
	height:900px!important;
	}
	#background, .background-class{
	
		margin-top: 5px!important;
		/*position: absolute!important;*/
		position:relative!important;
		/*position:absolute;*/
		background-image: url('data:image/png;base64,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') !important;
		text-align:justify;
		z-index:0;
		background:white;
		/*display:block;*/
		min-height:50%; 
		/*max-width: 50% !important;*/
	}
	#background-backpage{
		text-align:justify;
		position:inherit;
		z-index:0;
		background:white;
		/*display:block;*/
		min-height:50%; 
		min-width:100%;
	}
	
	#podbox-inner{
	
	/*padding:10px;*/
	}
	#podbox{
		font-weight: bold;
	
		font-size: 10px;
	
		margin-top: 20px!important;
		position: relative!important;
	
		/*position: relative;*/
	
		padding-top: 0px !important;
		z-index:1;
			border: 3px solid black;
		margin: 50px 50px;
		max-width: 85%;
			background-color: #ffffff;
				padding: 0px;
			border-top-left-radius: 20px;
		border-top-right-radius: 20px;}
	
	#bg-text
	{
	  color: #e3e3e3!important;
	font-family: "Source Sans Pro";
	font-size: 12px!important;
	font-weight: 700!important;
	text-transform: uppercase!important;
	/* Text style for "NTEX TRANS" */
	letter-spacing: 0.15px!important;
	z-index: 0 !important;
	background-color: white !important;
	
	}
	#bg-text2
	{
	  color: #e3e3e3!important;
	font-family: "Source Sans Pro";
	font-size: 12px!important;
	font-weight: 700!important;
	text-transform: uppercase!important;
	/* Text style for "NTEX TRANS" */
	letter-spacing: 0.15px!important;
	background-color: white !important;
	z-index: 1 !important;
	
	
	}
	.pod-top{
	  font-size: 20px;
	  font-weight: bold;
	  border-top-left-radius: 16px;
	  border-top-right-radius: 16px;
	  background-color:  black !important;
	  color: white !important;
	  text-align:  center !important;
	  margin: 0px !important;
	  padding: 5px;
	}
	
	.trip-no-backpage{
	  border: 2px solid lightgrey; 
	  border-radius: 12px;
	  color:lightgrey !important;
	  font-size: 22px !important;
	  width: 160px;
	  font-weight: bold;
	  text-align: center;
	  background-color: white !important;
	  /*position: fixed;*/
	  margin-top: 20px !important;
	  margin-left: 20px !important;
	  margin-right: 20px !important;

	}
	.lighttext{
	color: lightgrey !important;
	text-align: center !important;
	}
	
	.borderLeft {
		border-right: 1px solid lightgrey !important;
		margin-right: 20px;
		padding-right: 20px;
	
	
	}
	
	.lr-top-left{
	color: #000000;
	font-family: "Source Sans Pro Extra Light";
	font-size: 14px;
	font-weight: 200;
	
	}
	.lr-top-left-light{
	color: #000000 !important;
	font-family: "Source Sans Pro Extra Light";
	font-size: 14px;
	font-weight: 200;
	text-align: center !important;
	padding-right: 0px!important;
	
	}
	.lr-top{
	  /* Style for "LR-07981" */
	color: #000000;
	font-family: "Source Sans Pro Extra Light";
	font-size: 14px!important;
	font-weight: 700;
	text-transform: uppercase;
	}
	#print-format label, .print-format label {
	  color: #000000;
	  /*font-family: "Source Sans Pro";*/
	  font-size: 11px!important;
	  font-weight: bold!important;
	  /*line-height: 11px !important;*/
	}
	.col-xs-7, .col-xs-12  {
		/*font-family: Source Sans Pro;*/
		font-style: normal;
		font-weight: normal;
		line-height: 13px!important;
		font-size: 11px!important;
		color: #000000 !important;
	}
	.ntex-address {
	  color: #000000;
	  font-family: "Source Sans Pro";
	  font-size: 11px;
	  font-weight: 400;
	}
	.ntex-name{
	  color: #000000;
	  font-family: "Source Sans Pro";
	  font-size: 11px;
	  font-weight: 700;
	}
	
	.pkg td {
	  /*font-family: "Source Sans Pro Semi Bold";*/
	  font-size: 11px;
	  font-weight: 600;
	}
    </style>
    <div id="header-html_custom" style="margin-top:20px !important">
     <header id="pageHeader">
      <table width="100% !important">
       <tbody>
        <tr width="100% !important">
         <td width="55% !important">
          <img src="https://with.run/images/logo-full.png" style="width: 207px; height: 50.9686px;"/>
         </td>
         <td class="text-right lr-top-left-light" width="30%!important">
          Consignee Copy
          <span style="float: right;margin-right: -10px;">
           |
          </span>
         </td>
         <td class="text-center lr-top" width="15%!important">
          LR-00104
         </td>
        </tr>
       </tbody>
      </table>
      <table width="100% !important">
       <tbody>
        <tr width="100% !important">
         <td class="borderLeft" width="85%">
          <p class="ntex-name">
           <b>
            NTEx Transportation Services Pvt Ltd
           </b>
          </p>
          <p class="ntex-address">
           Unit 16, Ganesham Phase 2, Building D, Fourth Floor,
           <br/>
           Pimple Saudagar, Pune, 411027
           <br/>
           <b>
            State:
           </b>
           Maharashtra
           <br/>
           <b>
            GSTN:
           </b>
           27AAUCS5079A1ZZ
          </p>
         </td>
         <td class="text-center" style="padding-left:0px!important" width="15%">
          <img draggable="false" src="https://gamma-velocity.elasticrun.in/api/method/erun_util.util.qr_code.qrcode_gen?string=LR-00104&amp;size=4&amp;ecclevel=2" style="width:70% !important"/>
         </td>
        </tr>
       </tbody>
      </table>
      <hr style="margin-top:0px;margin-bottom:0px;border-top:1px solid black !important;"/>
      <div class="row">
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5">
          <h4>
           Lorry Receipt
          </h4>
         </div>
         <div class="col-xs-7">
          <h4>
           (LR-00104)
          </h4>
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Vehicle Number
          </label>
         </div>
         <div class="col-xs-7">
          KA44DF4534
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Trip Number
          </label>
         </div>
         <div class="col-xs-7">
          NTPL-00089
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Load From
          </label>
         </div>
         <div class="col-xs-7">
          Bangalore,Karnataka
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Load To
          </label>
         </div>
         <div class="col-xs-7">
          Pune,Maharashtra
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Date
          </label>
         </div>
         <div class="col-xs-7">
          20-11-2019
         </div>
        </div>
       </div>
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5">
          <h4>
           Insurance
          </h4>
         </div>
         <div class="col-xs-7">
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Shipper's risk
          </label>
         </div>
         <div class="col-xs-7">
         </div>
        </div>
        <div class="row">
         <div class="col-xs-12">
          The consignor has stated that he has insured/not insured the consignment
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Company
          </label>
         </div>
         <div class="col-xs-7">
          Patanjali Ayurved Pvt Ltd
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Policy Number
          </label>
         </div>
         <div class="col-xs-7">
         </div>
        </div>
       </div>
      </div>
      <br/>
      <hr style="margin-top:0px;margin-bottom:0px;border-top:1px solid gray !important;"/>
      <br/>
      <div class="row">
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5">
          <label>
           Consignor
          </label>
         </div>
         <div class="col-xs-7">
          <label>
           Patanjali Warehouse
          </label>
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Address
          </label>
         </div>
         <div class="col-xs-7">
          Patanjali Warehouse
No 7,
Bellandur
Pin: 560110
City: Bangalore,Karnataka
GSTN: NA
         </div>
        </div>
       </div>
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5">
          <label>
           Consignee
          </label>
         </div>
         <div class="col-xs-7">
          <label>
           Patanjali Retail Center
          </label>
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Address
          </label>
         </div>
         <div class="col-xs-7">
          Patanjali Retail Center
No 9,
Pimple Saudagar
Pin: 410012
City: Pune,Maharashtra
GSTN: NA
         </div>
        </div>
       </div>
      </div>
      <hr style="margin-top:0px;margin-bottom:0px;border-top:1px solid gray !important;"/>
      <div class="row">
       <div class="col-xs-5">
        <h4>
         Goods Details
        </h4>
       </div>
       <div class="col-xs-7">
       </div>
      </div>
      <div class="row">
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5">
          <label>
           Value of Goods (₹)
          </label>
         </div>
         <div class="col-xs-7">
          1,25,000.00
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Invoice Date
          </label>
         </div>
         <div class="col-xs-7">
          20-11-2019
         </div>
        </div>
       </div>
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5" style="word-break:break-all">
          <label>
           Invoice Numbers
          </label>
         </div>
         <div class="col-xs-7" style="word-break:break-all">
          GRE-456723456
         </div>
        </div>
       </div>
      </div>
      <br/>
      <table class="table pkg" style="margin:0px!important;">
       <tbody>
        <tr>
         <td style="border-top:none !important;">
          Sr
         </td>
         <td style="border-top:none !important;">
          Number of Packages
         </td>
         <td style="border-top:none !important;">
          Method of Packing
         </td>
         <td style="border-top:none !important;">
          Actual Weight
         </td>
         <td style="border-top:none !important;">
          Unit
         </td>
        </tr>
        <tr>
         <td style="border-top: 1px solid #051a29!important;">
          1
         </td>
         <td style="border-top: 1px solid #051a29!important;">
          12
         </td>
         <td style="border-top: 1px solid #051a29!important;">
          CB
         </td>
         <td style="border-top: 1px solid #051a29!important;">
          12
         </td>
         <td style="border-top: 1px solid #051a29!important;">
          Tonnes
         </td>
        </tr>
       </tbody>
      </table>
     </header>
    </div>
    <!-- top section -->
    <div class="bg-top-class" id="background">
     <div id="podbox">
      <p class="pod-top">
       POD Acknowledgement Section
      </p>
      <div id="podbox-inner">
       <table class="table table-bordered" style="margin-bottom:0px !important;
							  margin-top: 0px;">
        <tbody>
         <tr>
          <td colspan="2" width="25%">
           Arrival Date
          </td>
          <td colspan="2" width="25%">
           <p class="lighttext">
            DD MM YY
           </p>
          </td>
          <td colspan="2" width="25%">
           Arrival Time
          </td>
          <td colspan="2" width="25%">
           <p class="lighttext">
            HH MM
           </p>
          </td>
         </tr>
         <tr>
          <td colspan="2">
           Vehicle Release Date
          </td>
          <td colspan="2">
           <p class="lighttext">
            DD MM YY
           </p>
          </td>
          <td colspan="2">
           Vehicle Release Time
          </td>
          <td colspan="2">
           <p class="lighttext">
            HH MM
           </p>
          </td>
         </tr>
         <tr>
          <td colspan="2">
           Detention Time/Days
          </td>
          <td colspan="2">
          </td>
          <td colspan="4">
           One Time Seal Number (OTS) :
          </td>
         </tr>
         <tr>
          <td colspan="4" rowspan="3">
           Stamp and Signature
          </td>
          <td colspan="4">
           Received Goods with Proper One Time Seal?
           <br/>
           <p>
            <input name="checkbox" type="checkbox" value="value"/>
            Yes
            <input name="checkbox" type="checkbox" value="value"/>
            No
           </p>
          </td>
         </tr>
         <tr>
          <td colspan="2">
           No of packages Received
          </td>
          <td colspan="2">
          </td>
         </tr>
         <tr>
          <td colspan="2">
           Unloading Charges (If paid by the transporter)
          </td>
          <td colspan="2">
          </td>
         </tr>
         <tr>
          <td colspan="8">
           Remarks
           <br/>
           <br/>
           <br/>
          </td>
         </tr>
        </tbody>
       </table>
      </div>
     </div>
    </div>
    <div class="page-break">
    </div>
    <!--<div id="background-backpage" class="background-class">
	<div class="row">
		<div class="col-xs-6 text-left">
			<span class="trip-no-backpage">NTPL-00089 </span>
		</div>
		<div class="col-xs-6 text-right">
			<span class="trip-no-backpage">LR-00104</span>
		</div>
	</div>

</div>-->
    <div class="empty-background-class" id="background-backpage">
    </div>
    <div class="page-break">
    </div>
    <div id="header-html_custom" style="margin-top:20px !important">
     <header id="pageHeader">
      <table width="100% !important">
       <tbody>
        <tr width="100% !important">
         <td width="55% !important">
          <img src="https://with.run/images/logo-full.png" style="width: 207px; height: 50.9686px;"/>
         </td>
         <td class="text-right lr-top-left-light" width="30%!important">
          Consignor Copy
          <span style="float: right;margin-right: -10px;">
           |
          </span>
         </td>
         <td class="text-center lr-top" width="15%!important">
          LR-00104
         </td>
        </tr>
       </tbody>
      </table>
      <table width="100% !important">
       <tbody>
        <tr width="100% !important">
         <td class="borderLeft" width="85%">
          <p class="ntex-name">
           <b>
            NTEx Transportation Services Pvt Ltd
           </b>
          </p>
          <p class="ntex-address">
           Unit 16, Ganesham Phase 2, Building D, Fourth Floor,
           <br/>
           Pimple Saudagar, Pune, 411027
           <br/>
           <b>
            State:
           </b>
           Maharashtra
           <br/>
           <b>
            GSTN:
           </b>
           27AAUCS5079A1ZZ
          </p>
         </td>
         <td class="text-center" style="padding-left:0px!important" width="15%">
          <img draggable="false" src="https://gamma-velocity.elasticrun.in/api/method/erun_util.util.qr_code.qrcode_gen?string=LR-00104&amp;size=4&amp;ecclevel=2" style="width:70% !important"/>
         </td>
        </tr>
       </tbody>
      </table>
      <hr style="margin-top:0px;margin-bottom:0px;border-top:1px solid black !important;"/>
      <div class="row">
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5">
          <h4>
           Lorry Receipt
          </h4>
         </div>
         <div class="col-xs-7">
          <h4>
           (LR-00104)
          </h4>
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Vehicle Number
          </label>
         </div>
         <div class="col-xs-7">
          KA44DF4534
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Trip Number
          </label>
         </div>
         <div class="col-xs-7">
          NTPL-00089
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Load From
          </label>
         </div>
         <div class="col-xs-7">
          Bangalore,Karnataka
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Load To
          </label>
         </div>
         <div class="col-xs-7">
          Pune,Maharashtra
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Date
          </label>
         </div>
         <div class="col-xs-7">
          20-11-2019
         </div>
        </div>
       </div>
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5">
          <h4>
           Insurance
          </h4>
         </div>
         <div class="col-xs-7">
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Shipper's risk
          </label>
         </div>
         <div class="col-xs-7">
         </div>
        </div>
        <div class="row">
         <div class="col-xs-12">
          The consignor has stated that he has insured/not insured the consignment
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Company
          </label>
         </div>
         <div class="col-xs-7">
          Patanjali Ayurved Pvt Ltd
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Policy Number
          </label>
         </div>
         <div class="col-xs-7">
         </div>
        </div>
       </div>
      </div>
      <br/>
      <hr style="margin-top:0px;margin-bottom:0px;border-top:1px solid gray !important;"/>
      <br/>
      <div class="row">
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5">
          <label>
           Consignor
          </label>
         </div>
         <div class="col-xs-7">
          <label>
           Patanjali Warehouse
          </label>
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Address
          </label>
         </div>
         <div class="col-xs-7">
          Patanjali Warehouse
No 7,
Bellandur
Pin: 560110
City: Bangalore,Karnataka
GSTN: NA
         </div>
        </div>
       </div>
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5">
          <label>
           Consignee
          </label>
         </div>
         <div class="col-xs-7">
          <label>
           Patanjali Retail Center
          </label>
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Address
          </label>
         </div>
         <div class="col-xs-7">
          Patanjali Retail Center
No 9,
Pimple Saudagar
Pin: 410012
City: Pune,Maharashtra
GSTN: NA
         </div>
        </div>
       </div>
      </div>
      <hr style="margin-top:0px;margin-bottom:0px;border-top:1px solid gray !important;"/>
      <div class="row">
       <div class="col-xs-5">
        <h4>
         Goods Details
        </h4>
       </div>
       <div class="col-xs-7">
       </div>
      </div>
      <div class="row">
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5">
          <label>
           Value of Goods (₹)
          </label>
         </div>
         <div class="col-xs-7">
          1,25,000.00
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Invoice Date
          </label>
         </div>
         <div class="col-xs-7">
          20-11-2019
         </div>
        </div>
       </div>
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5" style="word-break:break-all">
          <label>
           Invoice Numbers
          </label>
         </div>
         <div class="col-xs-7" style="word-break:break-all">
          GRE-456723456
         </div>
        </div>
       </div>
      </div>
      <br/>
      <table class="table pkg" style="margin:0px!important;">
       <tbody>
        <tr>
         <td style="border-top:none !important;">
          Sr
         </td>
         <td style="border-top:none !important;">
          Number of Packages
         </td>
         <td style="border-top:none !important;">
          Method of Packing
         </td>
         <td style="border-top:none !important;">
          Actual Weight
         </td>
         <td style="border-top:none !important;">
          Unit
         </td>
        </tr>
        <tr>
         <td style="border-top: 1px solid #051a29!important;">
          1
         </td>
         <td style="border-top: 1px solid #051a29!important;">
          12
         </td>
         <td style="border-top: 1px solid #051a29!important;">
          CB
         </td>
         <td style="border-top: 1px solid #051a29!important;">
          12
         </td>
         <td style="border-top: 1px solid #051a29!important;">
          Tonnes
         </td>
        </tr>
       </tbody>
      </table>
     </header>
    </div>
    <!-- top section -->
    <div class="bg-top-class" id="background">
     <div id="podbox">
      <p class="pod-top">
       POD Acknowledgement Section
      </p>
      <div id="podbox-inner">
       <table class="table table-bordered" style="margin-bottom:0px !important;
							  margin-top: 0px;">
        <tbody>
         <tr>
          <td colspan="2" width="25%">
           Arrival Date
          </td>
          <td colspan="2" width="25%">
           <p class="lighttext">
            DD MM YY
           </p>
          </td>
          <td colspan="2" width="25%">
           Arrival Time
          </td>
          <td colspan="2" width="25%">
           <p class="lighttext">
            HH MM
           </p>
          </td>
         </tr>
         <tr>
          <td colspan="2">
           Vehicle Release Date
          </td>
          <td colspan="2">
           <p class="lighttext">
            DD MM YY
           </p>
          </td>
          <td colspan="2">
           Vehicle Release Time
          </td>
          <td colspan="2">
           <p class="lighttext">
            HH MM
           </p>
          </td>
         </tr>
         <tr>
          <td colspan="2">
           Detention Time/Days
          </td>
          <td colspan="2">
          </td>
          <td colspan="4">
           One Time Seal Number (OTS) :
          </td>
         </tr>
         <tr>
          <td colspan="4" rowspan="3">
           Stamp and Signature
          </td>
          <td colspan="4">
           Received Goods with Proper One Time Seal?
           <br/>
           <p>
            <input name="checkbox" type="checkbox" value="value"/>
            Yes
            <input name="checkbox" type="checkbox" value="value"/>
            No
           </p>
          </td>
         </tr>
         <tr>
          <td colspan="2">
           No of packages Received
          </td>
          <td colspan="2">
          </td>
         </tr>
         <tr>
          <td colspan="2">
           Unloading Charges (If paid by the transporter)
          </td>
          <td colspan="2">
          </td>
         </tr>
         <tr>
          <td colspan="8">
           Remarks
           <br/>
           <br/>
           <br/>
          </td>
         </tr>
        </tbody>
       </table>
      </div>
     </div>
    </div>
    <div class="page-break">
    </div>
    <!--<div id="background-backpage" class="background-class">
	<div class="row">
		<div class="col-xs-6 text-left">
			<span class="trip-no-backpage">NTPL-00089 </span>
		</div>
		<div class="col-xs-6 text-right">
			<span class="trip-no-backpage">LR-00104</span>
		</div>
	</div>

</div>-->
    <div class="empty-background-class" id="background-backpage">
    </div>
    <div class="page-break">
    </div>
    <div id="header-html_custom" style="margin-top:20px !important">
     <header id="pageHeader">
      <table width="100% !important">
       <tbody>
        <tr width="100% !important">
         <td width="55% !important">
          <img src="https://with.run/images/logo-full.png" style="width: 207px; height: 50.9686px;"/>
         </td>
         <td class="text-right lr-top-left-light" width="30%!important">
          POD Copy
          <span style="float: right;margin-right: -10px;">
           |
          </span>
         </td>
         <td class="text-center lr-top" width="15%!important">
          LR-00104
         </td>
        </tr>
       </tbody>
      </table>
      <table width="100% !important">
       <tbody>
        <tr width="100% !important">
         <td class="borderLeft" width="85%">
          <p class="ntex-name">
           <b>
            NTEx Transportation Services Pvt Ltd
           </b>
          </p>
          <p class="ntex-address">
           Unit 16, Ganesham Phase 2, Building D, Fourth Floor,
           <br/>
           Pimple Saudagar, Pune, 411027
           <br/>
           <b>
            State:
           </b>
           Maharashtra
           <br/>
           <b>
            GSTN:
           </b>
           27AAUCS5079A1ZZ
          </p>
         </td>
         <td class="text-center" style="padding-left:0px!important" width="15%">
          <img draggable="false" src="https://gamma-velocity.elasticrun.in/api/method/erun_util.util.qr_code.qrcode_gen?string=LR-00104&amp;size=4&amp;ecclevel=2" style="width:70% !important"/>
         </td>
        </tr>
       </tbody>
      </table>
      <hr style="margin-top:0px;margin-bottom:0px;border-top:1px solid black !important;"/>
      <div class="row">
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5">
          <h4>
           Lorry Receipt
          </h4>
         </div>
         <div class="col-xs-7">
          <h4>
           (LR-00104)
          </h4>
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Vehicle Number
          </label>
         </div>
         <div class="col-xs-7">
          KA44DF4534
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Trip Number
          </label>
         </div>
         <div class="col-xs-7">
          NTPL-00089
         </div>
        </div>
        <!-- <div class="row">
					<div class="col-xs-5"><label>Shipment Number</label></div>
					<div class="col-xs-7 ">PATANJALI - 00008
					</div>
				</div> -->
        <div class="row">
         <div class="col-xs-5">
          <label>
           Load From
          </label>
         </div>
         <div class="col-xs-7">
          Bangalore,Karnataka
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Load To
          </label>
         </div>
         <div class="col-xs-7">
          Pune,Maharashtra
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Date
          </label>
         </div>
         <div class="col-xs-7">
          20-11-2019
         </div>
        </div>
       </div>
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5">
          <h4>
           Insurance
          </h4>
         </div>
         <div class="col-xs-7">
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Shipper's risk
          </label>
         </div>
         <div class="col-xs-7">
         </div>
        </div>
        <div class="row">
         <div class="col-xs-12">
          The consignor has stated that he has insured/not insured the consignment
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Company
          </label>
         </div>
         <div class="col-xs-7">
          Patanjali Ayurved Pvt Ltd
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Policy Number
          </label>
         </div>
         <div class="col-xs-7">
         </div>
        </div>
       </div>
      </div>
      <br/>
      <hr style="margin-top:0px;margin-bottom:0px;border-top:1px solid gray !important;"/>
      <br/>
      <div class="row">
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5">
          <label>
           Consignor
          </label>
         </div>
         <div class="col-xs-7">
          <label>
           Patanjali Warehouse
          </label>
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Address
          </label>
         </div>
         <div class="col-xs-7">
          Patanjali Warehouse
No 7,
Bellandur
Pin: 560110
City: Bangalore,Karnataka
GSTN: NA
         </div>
        </div>
       </div>
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5">
          <label>
           Consignee
          </label>
         </div>
         <div class="col-xs-7">
          <label>
           Patanjali Retail Center
          </label>
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Address
          </label>
         </div>
         <div class="col-xs-7">
          Patanjali Retail Center
No 9,
Pimple Saudagar
Pin: 410012
City: Pune,Maharashtra
GSTN: NA
         </div>
        </div>
       </div>
      </div>
      <hr style="margin-top:0px;margin-bottom:0px;border-top:1px solid gray !important;"/>
      <div class="row">
       <div class="col-xs-5">
        <h4>
         Goods Details
        </h4>
       </div>
       <div class="col-xs-7">
       </div>
      </div>
      <div class="row">
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5">
          <label>
           Value of Goods (₹)
          </label>
         </div>
         <div class="col-xs-7">
          1,25,000.00
         </div>
        </div>
        <div class="row">
         <div class="col-xs-5">
          <label>
           Invoice Date
          </label>
         </div>
         <div class="col-xs-7">
          20-11-2019
         </div>
        </div>
       </div>
       <div class="col-xs-6">
        <div class="row">
         <div class="col-xs-5" style="word-break:break-all">
          <label>
           Invoice Numbers
          </label>
         </div>
         <div class="col-xs-7" style="word-break:break-all">
          GRE-456723456
         </div>
        </div>
       </div>
      </div>
      <br/>
      <table class="table pkg" style="margin:0px!important;">
       <tbody>
        <tr>
         <td style="border-top:none !important;">
          Sr
         </td>
         <td style="border-top:none !important;">
          Number of Packages
         </td>
         <td style="border-top:none !important;">
          Method of Packing
         </td>
         <td style="border-top:none !important;">
          Actual Weight
         </td>
         <td style="border-top:none !important;">
          Unit
         </td>
        </tr>
        <tr>
         <td style="border-top: 1px solid #051a29!important;">
          1
         </td>
         <td style="border-top: 1px solid #051a29!important;">
          12
         </td>
         <td style="border-top: 1px solid #051a29!important;">
          CB
         </td>
         <td style="border-top: 1px solid #051a29!important;">
          12
         </td>
         <td style="border-top: 1px solid #051a29!important;">
          Tonnes
         </td>
        </tr>
       </tbody>
      </table>
     </header>
    </div>
    <!-- top section -->
    <div class="bg-top-class" id="background">
     <div id="podbox">
      <p class="pod-top">
       POD Acknowledgement Section
      </p>
      <div id="podbox-inner">
       <table class="table table-bordered" style="margin-bottom:0px !important;
							  margin-top: 0px;">
        <tbody>
         <tr>
          <td colspan="2" width="25%">
           Arrival Date
          </td>
          <td colspan="2" width="25%">
           <p class="lighttext">
            DD MM YY
           </p>
          </td>
          <td colspan="2" width="25%">
           Arrival Time
          </td>
          <td colspan="2" width="25%">
           <p class="lighttext">
            HH MM
           </p>
          </td>
         </tr>
         <tr>
          <td colspan="2">
           Vehicle Release Date
          </td>
          <td colspan="2">
           <p class="lighttext">
            DD MM YY
           </p>
          </td>
          <td colspan="2">
           Vehicle Release Time
          </td>
          <td colspan="2">
           <p class="lighttext">
            HH MM
           </p>
          </td>
         </tr>
         <tr>
          <td colspan="2">
           Detention Time/Days
          </td>
          <td colspan="2">
          </td>
          <td colspan="4">
           One Time Seal Number (OTS) :
          </td>
         </tr>
         <tr>
          <td colspan="4" rowspan="3">
           Stamp and Signature
          </td>
          <td colspan="4">
           Received Goods with Proper One Time Seal?
           <br/>
           <p>
            <input name="checkbox" type="checkbox" value="value"/>
            Yes
            <input name="checkbox" type="checkbox" value="value"/>
            No
           </p>
          </td>
         </tr>
         <tr>
          <td colspan="2">
           No of packages Received
          </td>
          <td colspan="2">
          </td>
         </tr>
         <tr>
          <td colspan="2">
           Unloading Charges (If paid by the transporter)
          </td>
          <td colspan="2">
          </td>
         </tr>
         <tr>
          <td colspan="8">
           Remarks
           <br/>
           <br/>
           <br/>
          </td>
         </tr>
        </tbody>
       </table>
      </div>
     </div>
    </div>
    <div class="page-break">
    </div>
    <div class="background-class" id="background-backpage">
     <div class="row">
      <div class="col-xs-6 text-left">
       <span class="trip-no-backpage">
        NTPL-00089
       </span>
      </div>
      <div class="col-xs-6 text-right">
       <span class="trip-no-backpage">
        LR-00104
       </span>
      </div>
     </div>
    </div>
    <!--<hr style="margin-top:15px;margin-bottom:0px;border-top:1px solid black !important;">
	<div class="row" style="margin-top:10px;"> 
		<div class="col-md-6 col-lg-6 col-xs-6">
			<b>Please Dispatch the POD copy to below Address:<br/></b>
			karthikeyan.y@elastic.run<br/>
			karthikeyan.y@elastic.run
Ntex Transportation Services Pvt. Ltd.
Ganesham Phase 2, Building D,Unit no.16, Fourth Floor, Pimple Saudagar.
Pin: 411027
City: Pune,Maharashtra
GSTN: 27AAUCS5079A1ZZ
Contact:-8754294001<br/>
			<b>Ph:</b> 8754294001
		</div>
		
		<div class="col-md-6 col-lg-6 col-xs-6">
			
		</div>



	</div>-->
   </div>
  </div>
  <script>
   document.addEventListener('DOMContentLoaded', () => {
			const page_div = document.querySelector('.page-break');

			page_div.style.display = 'flex';
			page_div.style.flexDirection = 'column';

			const footer_html = document.getElementById('footer-html');
			footer_html.classList.add('hidden-pdf');
			footer_html.classList.remove('visible-pdf');
			footer_html.style.order = 1;
			footer_html.style.marginTop = '20px';
		});
  </script>
 </body>
 <!-- karthikeyan.y@elastic.run -->
</html>""" 
fname = "/tmp/frappe-pdf-0c523a5fa3744b4310b656414b3d8e9b957b86805d322c9254797e4f.pdf" 
pdfkit.from_string(html, fname, options=options or {})
