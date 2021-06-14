package com.example.basic_3_recycleview

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.recyclerview.widget.GridLayoutManager
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.activity_main.*
import org.jetbrains.anko.longToast
import org.jetbrains.anko.toast

class MainActivity : AppCompatActivity() {
    val items = mutableListOf<MainData>()
    init {
        for(i in 1..70){
            items += MainData("Title$i", "Content$i")
        }
    }
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        rv_main_list.adapter = MainAdapter(items, ::onItemClick)
//        rv_main_list.layoutManager = LinearLayoutManager(this)
        rv_main_list.layoutManager = GridLayoutManager(this,2)

        btn.setOnClickListener {
            val data = MainData(main_title.text.toString(), main_content.text.toString())
            items.add(0, data)
            longToast(data.toString())

            // 수정 수 adapter에게 통지하고, 화면 갱신을 해야 함
            rv_main_list.adapter?.notifyDataSetChanged()
            main_title.text.clear()     // 새로고침 후 텍스트 초기화
            main_content.text.clear()
        }
    }
    fun onItemClick(pos: Int){
        val data = items[pos]
//        toast(data.toString())

        startAvtivity<DetailActivity>(
            "KEY_DATA" to data
        )
    }
}