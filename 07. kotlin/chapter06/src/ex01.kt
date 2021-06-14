fun readline(): String ? {
    return null
}
fun main(args: Array<String>) {
    var beverage: String?
    beverage = readLine()?.capitalize()
//    beverage = null
    println(beverage)
}