
fun main(args: Array<String>) {
//    for(patron in patronList2) {
//        println("좋은 밤입니다. $patron 님")
//    }
//
//    patronList2.forEach{ patron -> println("좋은 밤입니다. $patron")}
//
//    patronList2.forEach{ println("좋은 밤입니다. $it 님")}
//
//    patronList2.forEachIndexed{ index, patron ->
//        println("좋은 밤입니다. $patron 님 - 당신은 ${index+1}번째 입니다.")}

    var map = mapOf<String, Double>(
//        "Eli" to 10.5,
//        "Sophie" to 5
        Pair("Eli", 10.5),
        Pair("Sophie", 5.5)
    )
    map += "Sophie2" to 6.0
    println(map)

    var value: Double   // null 허용 안함
    println(map)
    value = map.getOrElse("Sophie2"){ 0.0 }
    println(value)
    value = map.getOrDefault("test", 0.0)
    println(value)
    println()

    // forEach로 Map 순회하면서 출력
    map.forEach{ key, value ->
        println("$key : $value")
    }
}