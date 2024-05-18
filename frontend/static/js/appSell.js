function Sell_Product () {
    let id = document.getElementById("id").value
    let obj_id = {"id": id}
    fetch("/consult_user", {
        "method" : "post",
        "headers" : {"content-type":"application/json"},
        "body" : JSON.stringify(obj_id)
    })
    .then(resp => resp.json())
    .then(data => {
        if(data.status == "ok"){
            obj_data = data.name + " " + data.category + " " + data.price
            document.getElementById("txt_data").value = obj_data
            document.getElementById("foto_user").src = 'https://my-repo-imagenes-aws-curso.s3.amazonaws.com/' + data.photo
            
        }
        else{
            alert("The user wasnt found")
        }
    })
    .catch(err => alert(err))
}
