google.load('visualization', '1.1', {packages: ['line']});
google.setOnLoadCallback(drawChart);

function process_query(){

	var query = $('#query').val()

	$.ajax({
		data: {
			query : query,
		},
		success: function(data){
			// Success
			console.log("Successfully received updated recommendations");
			console.log(data)
			console.log(data.results);

			$("#selectedtags").empty();
			$('#statsdiv').empty();
			if(data.results.length<=0){
				$("#selectedtags").append('<div class="col-xs-12 text-center"><h3>No tags found!</h3></div>');
			}
			else{
				$("#selectedtags").append('<div class="col-xs-4 col-xs-offset-5" id="tagpills"></div>')
				for(var i=0; i<data.results.length; i++) {
					$("#tagpills").append('<div class="checkbox"> <label><input type="checkbox" name="seltag" value="'+data.results[i]+'">'+data.results[i]+'</label> </div>')
				}
				$("#tagpills").append('<div class="col-xs-12"><button class="btn btn-default" onclick="get_stats()">Get Stats</button></div><hr/>')
			}
		},
		error: function(){
			console.log("nooo :(");
		},
		type: 'GET'
	});
};

function get_stats(){

	var selected = [];

	$.each($('input[name="seltag"]:checked'), function(){
		console.log($(this))

		selected.push($(this).val());
	});

	$.ajax({
		data: {
			selected : selected,
		},
		success: function(data){
			// Success
			console.log("Successfully received updated recommendations");
			console.log(data)

			$('#statsdiv').empty();
			//per tag
			for(var i=0; i<data.results.length;i++){
				var tagname = data.results[i][0].tag
				// Aggregate results
				var total_questions = 0
				var total_answers = 0
				var accepted_answers = 0
				var closed_questions = 0
				var open_questions = 0
				var users = 0
				var chance = 0

				var trend_rows = []
				// per year per tag
				for(var j=0; j<data.results[i].length; j++){
					var trend_row = []
					trend_row.push(data.results[i][j].year.toString())
					trend_row.push(data.results[i][j].total_questions)
					trend_row.push(data.results[i][j].total_answers)
					trend_row.push(data.results[i][j].accepted_answers)
					trend_row.push(data.results[i][j].closed_questions)
					trend_row.push(data.results[i][j].open_questions)
					trend_row.push(data.results[i][j].users)
					trend_rows.push(trend_row)

					total_questions+=data.results[i][j].total_questions
					total_answers+=data.results[i][j].total_answers
					accepted_answers+=data.results[i][j].accepted_answers
					closed_questions+=data.results[i][j].closed_questions
					open_questions+=data.results[i][j].open_questions
					users+=data.results[i][j].users
				}

				chance = Math.round((accepted_answers/total_questions)*100)

				$('#statsdiv').append('<div class="col-xs-10 col-xs-offset1">'+
											'<h2>'+data.results[i][0].tag+'</h2>'+
											'<ul>'+
												'<li># Questions: '+total_questions+'</li>'+
												'<li># Answers: '+total_answers+'</li>'+
												'<li># Accepted Answers: '+accepted_answers+'</li>'+
												'<li># Closed Questions: '+closed_questions+'</li>'+
												'<li># Open Questions: '+open_questions+'</li>'+
												'<li># Active users: '+users+'</li>'+
												'<li># Chance of getting an answer : '+chance+' %</li>'+
											'</ul>'+
									'</div>');

				$('#statsdiv').append('<div class="col-xs-10 col-xs-offset1">'+
						'<h3>Top questions for '+tagname+'</h3>'+
						'<ul id="qlist-'+tagname+'"></ul>');
				for(var k=0;k<data.topq[tagname].length;k++){
					$('#qlist-'+tagname).append('<li><a href="http://stackoverflow.com/questions/'+data.topq[tagname][k].question_id+'" target="_blank">'+data.topq[tagname][k].title+'</a></li>')
				}

				$('#statsdiv').append('<div class="col-xs-10 col-xs-offset1">'+
						'<h3>Top users for '+tagname+'</h3>'+
						'<ul id="ulist-'+tagname+'"></ul>');
				for(var k=0;k<data.topu[tagname].length;k++){
					$('#ulist-'+tagname).append('<li><img src="http://storage.designcrowd.com/design_img/218612/137452/137452_2444148_218612_thumbnail.jpg" height="60" width="60" alt="No Image"/><a href="http://stackoverflow.com/users/'+data.topu[tagname][k].user_id+'" target="_blank">'+data.topu[tagname][k].displayname+'</a></li>')
				}

				var vizdata = new google.visualization.DataTable();
				vizdata.addColumn('string', 'Year');
			    vizdata.addColumn('number', '# Questions');
			    vizdata.addColumn('number', '# Answers');
			    vizdata.addColumn('number', '# Accepted Answers');
			    vizdata.addColumn('number', '# Closed Questions');
			    vizdata.addColumn('number', '# Open Questions');
			    vizdata.addColumn('number', '# Active Users');
			    vizdata.addRows(trend_rows)
			    console.log(trend_rows)
			    console.log(vizdata)
			    var options = {
			        chart: {
			          title: 'Trends for Tag: '+tagname,
			        },
			        width: 900,
			        height: 500,
			        axes: {
			          x: {
			            0: {side: 'top'}
			          }
			        }
			      };
			    $('#statsdiv').append('<div class="col-xs-12"><div id="'+data.results[i][0].tag+'"></div></div><hr/>')
			    var chart = new google.charts.Line(document.getElementById(data.results[i][0].tag));
			    chart.draw(vizdata, options);

			}
			
		},
		error: function(){
			console.log("nooo :(");
		},
		type: 'GET'
	});	
}