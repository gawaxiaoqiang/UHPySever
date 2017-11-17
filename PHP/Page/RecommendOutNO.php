<?php
require_once ('../Public_php/Globle_sc_fns.php');
/* 输出头部信息 */

$cssArr = array (
		'header.css',
		'UpdateData.css' 

);
$config = new ConfigINI ();
$cssabsArr = array (
	// $config->get ( 'URL.root_assets'. 'bootstrap-datetimepicker/css/datetimepicker.css')
);
$outPut = new OutPut ();
$jsArr = array (
		"RecommendOutNO.js" 
);
$jsabsArr = array (
		$outPut->getScriptStr ( $config->get ( 'URL.root_assets' ) . 'chart-master/Chart.js' ),
		"<script src=https://cdnjs.cloudflare.com/ajax/libs/socket.io/1.7.2/socket.io.js></script>" 

);

/* 输出顶部导航 */
$userimg = __getCookies ( 'userImg' );
$userName = __getCookies ( 'userName' );
$userInfo = array (
		"heardImg" => "fc3d.jpg",
		"userName" => $userName 
);

$outPut = new OutPut ();
$outPut->outPutHead ( $cssArr, $cssabsArr, "历史出球" );
$outPut->outPutHeader ( $userInfo );
$outPut->outSider ( "3D彩票" );
outmain ();
$outPut->outputFoot ( $jsArr, $jsabsArr );
function outmain() {
	?>
<section id="main-content">
	<section class="wrapper">

		<div class="row">
			<div class="col-lg-3 col-sm-3 col-md-3">
				<section id="main_silder" class="panel">
					<header class="panel-heading"> Category </header>
					<div class="panel-body">
						<ul class="nav prod-cat">
							<li><a href="./UpdateData.php"><i class=" fa fa-angle-right"></i>
									3D数据更新</a></li>
							<li><a class="active" href="./RecommendOutNO.php"><i
									class=" fa fa-angle-right"></i> 推荐数据</a></li>
							<li><a href="#"><i class=" fa fa-angle-right"></i> Beauty</a></li>
							<li><a href="#"><i class=" fa fa-angle-right"></i> Coat &amp;
									Jacket</a></li>
							<li><a href="#"><i class=" fa fa-angle-right"></i> Jeans</a></li>
							<li><a href="#"><i class=" fa fa-angle-right"></i> Jewellery</a></li>
							<li><a href="#"><i class=" fa fa-angle-right"></i> Electronics</a></li>
							<li><a href="#"><i class=" fa fa-angle-right"></i> Sports</a></li>
							<li><a href="#"><i class=" fa fa-angle-right"></i> Technology</a></li>
							<li><a href="#"><i class=" fa fa-angle-right"></i> Watches</a></li>
							<li><a href="#"><i class=" fa fa-angle-right"></i> Accessories</a></li>
						</ul>
					</div>
				</section>

			</div>
			<div class="col-lg-9 col-sm-9 col-md-9">
				<section class="panel">
					<header class="panel-heading">
						正确率评估 <span class="tools pull-right"> <input id="btnSend"
							type="button" value="开始" />
						</span>
					</header>
					<div></div>
				</section>
			</div>

			<div class="col-lg-9 col-sm-9 col-md-9">
				<section class="panel">
					<header class="panel-heading">
						正确率评估 <span class="tools pull-right"> </span>
					</header>

					<div class="easy-pie-chart">
						<div class="percentage easyPieChart" data-percent="36"
							style="width: 135px; height: 135px; line-height: 135px;">
							<span>35</span>%
				
						</div>
					</div>

				</section>


			</div>

			<div class="col-lg-9 col-sm-9 col-md-9">
				<section class="panel">
					<header class="panel-heading">
						来自服务端的消息 <span class="tools pull-right"> <a href="javascript:;"
							class="fa fa-chevron-down"></a> <a href="javascript:;"
							class="fa fa-remove"></a>
						</span>
					</header>
					<div class="panel-body">
						<textarea id="txtContent" cols="150" rows="10" readonly="readonly"
							class="comments"></textarea>
					</div>
				</section>
			</div>
			<div>
	
	</section>
</section>
<?php
}
?>