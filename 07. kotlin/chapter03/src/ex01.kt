fun main(args: Array<String>){
    val name = "마드리길"
    var healthPoints = 89
    val isBlessed = true
    val isImmortal = false

    //아우라
    val auraVisible = isBlessed && healthPoints> 50 || isImmortal
    val auraColor = if(auraVisible) "GREEN" else "NONE"
    println(auraColor)

    val healthStatus = when(healthPoints) {
        100 -> "최상의 상태!"

        in 90..99 -> "약간의 철과장 발생"
        in 75..89 -> if (isBlessed) "경미한 상처 발생했지만 빠른 치유 가능"
        else "경미한 상처만 있음"
        in 15..74 -> "많이 다친 것 같음"
        else -> "최악의 상태"
    }
    // 플레이어 상태 출력
    println("(Aura: $auraColor)" +
    "(Blessed: ${if (isBlessed) "YES" else "NO"}")
    print("$name $healthStatus")
}