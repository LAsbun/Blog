KindEditor.ready(function(K) {
    K.create('textarea[name=content]',{
        width:800,
        height:200,
        uploadJson: '/admin/upload/kindeditor',
    });
});

KindEditor.ready(function(K){
    K.create('textarea[name=something_to_say]',{
        width:800,
        height:450,
        uploadJson: '/admin/upload/kindeditor',
    })
});