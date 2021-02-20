var yazı = $(".userlar p ")
kullanıcılar = []

for (i of yazı) {

    a = $(i).text()
    kullanıcılar.push(a)

}

console.log(kullanıcılar)
var text = $(".emailler p ")
mailler = []

for (i of text) {

    b = $(i).text()
    mailler.push(b)

}

console.log(mailler)

// // burda veritabanındakı user isimlerine baglı kullancııya 
// // o adı alamazsın dedik onu kontrolunu yapıyoruz ama baya
// // mesaketli 4 subat
// bosluk strıplemek lazım  $.trim(str)
// length ogrenmek lazım  length 

$(function() {
    signupBtn = $(".signupBtn")

    $("#id_username").attr("maxlength", 35)

    helptext = $(".helptext")
    helptext2 = $(".helptext2")



    $("#id_username").on("keyup paste change blur ", function() {
        value = $(this).val()
        uzunluk = $(this).val().length
        total_value = $.trim(value)
        total_uzunluk = total_value.length

        if (total_uzunluk == 0) {
            console.log("deger yok ")
            $(this).css("border-color", "red")
            $("#id_username").after(helptext.addClass("text-danger").html("Bu alan boş bırakılamaz "))

            signupBtn.attr("type", "button").css("background-color", "gray")

        } else if (kullanıcılar.includes(total_value)) {

            console.log("bu kullanıcı ismi mevcut baska deneyın ")
            $(this).css("border-color", "red")
            $("#id_username").after(helptext.addClass("text-danger").html("Bu kullanıcı adı alınmıs !! "))
        } else if (total_uzunluk < 6) {

            console.log("6 karakterden az olamaz ")
            $(this).css("border-color", "red")
            $("#id_username").after(helptext.addClass("text-danger").html("Bu alan 6 karakterden az olamaz  !! "))


        } else {
            console.log($(this).val())
            $(this).css("border-color", "rgb(1, 189, 1)")
            $("#id_username").after(helptext.html(""))


        }
        console.log($(this).val().length)

    })

    // EMAİL İNPUT İÇİN --------------------
    var testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;
    $("#id_email").on("change blur keyup paste", function() {

        emailvalue = $(this).val()
        console.log(emailvalue)
        console.log(testEmail.test(emailvalue))
        geçerliklik = testEmail.test(emailvalue)
        if (geçerliklik) {

            if (mailler.includes(emailvalue)) {

                // eger daha once bu email kullanılmıssa 
                $(this).css("border-color", "red")
                $("#id_email").after(helptext2.addClass("text-danger").html("Bu emaille sisteme kayıtlı  !! "))

            } else {
                $(this).css("border-color", "rgb(1, 189, 1)")
                $("#id_email").after(helptext2.html(''))

            }
        } else {
            if (emailvalue.length == 0) {

                $(this).css("border-color", "red")
                $("#id_email").after(helptext2.addClass("text-danger").html("Bu alan boş bırakılamaz   !! "))

            } else {

                $(this).css("border-color", "red")
                $("#id_email").after(helptext2.addClass("text-danger").html("Geçerli bir email giriniz  !! "))

            }

        }

    })

    // PASSWORD  İNPUT İÇİN --------------------
    // pare = $("#id_password").parent()

    // pare.on("mouseout", function() {
    //     console.log("cıktı ")
    //     $("#id_password").after($('.see').css("visibility", "hidden"))

    // })

    $("#id_password").on("keyup paste  change", function() {

        passvalue = $(this).val()
        console.log(passvalue)
        $("#id_password").after($('.see').css("visibility", "visible"))


    })




    $(".see").click(function() {
        console.log("tıkladıkla icona ")
        if ($("#id_password").attr("type") == "text") {
            $("#id_password").attr("type", "password")
            $(".see").removeClass("fa-eye-slash").addClass("fa-eye")

        } else {

            $("#id_password").attr("type", "text")
            $(".see").removeClass("fa-eye").addClass("fa-eye-slash")

        }
    })




    $("#id_confirm").on("keyup paste  change", function() {

        passvalue = $(this).val()
        console.log(passvalue)
        $("#id_confirm").after($('.see2').css("visibility", "visible"))




    })
    $("#id_confirm").blur(function() {

        if ($("#id_password").val() != $("#id_confirm").val()) {
            $("#id_password").css("border-color", "red")
            $("#id_confirm").css("border-color", "red")
            $("#id_confirm").after($(".helptext3").addClass("text-danger").html("Parolalar uyusmuyor"))

        } else {
            $("#id_confirm").after($(".helptext3").html(''))
            $("#id_password").css("border-color", "green")
            $("#id_confirm").css("border-color", "green")
        }
    })



    $(".see2").click(function() {
        console.log("tıkladıkla icona ")
        if ($("#id_confirm").attr("type") == "text") {
            $("#id_confirm").attr("type", "password")
            $(".see2").removeClass("fa-eye-slash").addClass("fa-eye")

        } else {

            $("#id_confirm").attr("type", "text")
            $(".see2").removeClass("fa-eye").addClass("fa-eye-slash")

        }
    })

    // $("form button").click(function() {
    //     $("form input").each(function() {

    //         if ($(this).css("border-color") == "rgb(255,0,0)") {

    //             $("form button").attr("type", "button").css("background-color", "gray")
    //         }
    //         console.log($(this).css("border-color"))
    //     })

    // })




})