class Player(_name: String,
             var healthPoints:Int,
             var isBlessed: Boolean,
             private val isImmortal: Boolean) {
    var name = _name
        get() = field.capitalize()
        set(value) {
            field = value.trim()
        }

    val hometown by lazy{selectHometown()}

    fun selectHometown(): String {
        return "Seoul"
    }
    init {
        println("init block")
        require(healthPoints > 0 , {"healthPoints는 0보다 커야 합니다."})
        require(name.isNotBlank(), {"플레이어 이름이 있어야 합니다."})
    }

    constructor(name:String) : this(name,
                healthPoints=100,
                isBlessed = true,
                isImmortal = false) {
        println("보조 생성자")
        if(name.toLowerCase() == "kar") healthPoints = 45
    }
    fun castFireball(numFireballs: Int = 2) =
        println("한 덩어리의 파이어볼이 나타난다. (x$numFireballs)")

}