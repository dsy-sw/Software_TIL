class TownSquare : Room("Town Square") {
    private val bellSound = "댕댕"
    override  val dangerLevel = super.dangerLevel -3
    override fun load() = "당신의 참여를 주민들이 다 함께 환영합니다." +
            ringBell()
   private fun ringBell() = "당신의 도착을 알립니다. $bellSound"
}

fun printRoomInfo(room: Room) {
    println(room.description())
    println(room.load())
}

fun main() {
    val ts = TownSquare()
    println(ts.description())
    println(ts.load())

    var room: Room
    room = TownSquare()     // 인스턴스가 어느 것인지에 따라 값이 달라짐, 부모 타입 변수로는 모든 자식을 참조할 수 있음
    println(room.load())
    room = Room("Foyer")
}