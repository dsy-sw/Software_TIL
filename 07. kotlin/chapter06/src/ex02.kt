fun main(args: Array<String>) {
    var beverage = readline()!!.let {
        if(it.isNotBlank()) {
            it.capitalize()
        } else {
            "맥주"
        }
    }
    println(beverage)
}