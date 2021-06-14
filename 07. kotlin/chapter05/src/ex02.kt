fun main(args: Array<String>){
    runSimulation("김선달", ::printConstructionCost) { playerName, numBuildings ->
        val currentYear = 2021
        println("$numBuildings 채의 건물이 추가됨")
        "SimVillage 방문을 환영합니다. $playerName!(copyright $currentYear)"
    }
}

//fun runSimulation(playerName: String, greetingFunction: (String, Int) -> String) {
//    val numBuildings = (1..3).shuffled().last()     // 1~3 중 무작위 선택
//    println(greetingFunction(playerName, numBuildings))
//}

fun printConstructionCost(numBuildings: Int) {
    val cost = 500
    println("건축 비용: ${cost * numBuildings}")
}

inline fun runSimulation(playerName: String, costPrinter: (Int) -> Unit, greetingFunction: (String, Int) -> String) {
    val numBuildings = (1..3).shuffled().last()
    costPrinter(numBuildings)
    println(greetingFunction(playerName, numBuildings))
}