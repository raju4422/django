$.ajaxcall = function(newurl,dataobject,callback) {
//			dataobject.<?php  echo $csrfName; ?>='<?php echo $csrfhash; ?>';
			$.ajax({
				url: newurl,
				data: dataobject,
				dataType: 'json',
				type: 'POST',
//				headers: { 'User-Type': 'Api','Auth-Token':'<?php $this->session->userdata('auth_token'); ?>' },
				beforeSend: function () {
//					$('.theme-loader').css('display', '');
				},
				complete: function () {
//					$('.theme-loader').css('display', 'none');
				},
				success: function (data) {
					if(data.flag==1)
					{
						callback(data);
					}
					else if(data.flag==2){
						swal("Warning!",data.msg,"warning")
					}
					else{
						swal("Error!",data.msg,"error")
					}
				},
				error: function () {
					swal("Error!","Something went wrong. Please check your internet connection","error");
				}
			})
		};