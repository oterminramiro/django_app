$(document).ready( function () {

	// Datatable
	$('#myTable').DataTable({
		"language": {
			"paginate": {
				"previous": "<i class='fas fa-angle-left'></i>",
				"next": "<i class='fas fa-angle-right'></i>"
			}
		}
	});

	// Modal
	$(".editForm").click(function(){
		event.preventDefault();
		var href = $(this).attr('href');
		$.ajax({
			url: href,
			error: function(response, error) {
				alert(error);
			}
		}).done(function(response) {
			$('#exampleModal').html(response);
			$("#exampleModal").modal("show");
		});
	});

	// Delete button
	$(".deleteButton").click(function(){
		event.preventDefault();
		swal({
			title: 'Are you sure?',
			text: "You won't be able to revert this!",
			type: 'warning',
			showCancelButton: true,
			buttonsStyling: false,
			confirmButtonClass: 'btn btn-danger',
			confirmButtonText: 'Yes, delete it!',
			cancelButtonClass: 'btn btn-secondary'
		}).then((result) => {
			if (result.value) {
				// Show confirmation
				var href = $(this).attr('href');
				$.ajax({
					type: "GET",
					url: href,
					success: function (data) {
						swal({
							title: 'Deleted!',
							text: 'Your file has been deleted.',
							type: 'success',
							buttonsStyling: false,
							confirmButtonClass: 'btn btn-primary'
						});
						location.reload();
					},
					error: function (data) {
						swal({
							title: 'Error!',
							type: 'danger',
							buttonsStyling: false,
							confirmButtonClass: 'btn btn-danger'
						});
						console.log(data);
					}
				});
			}
		})
	});
});
