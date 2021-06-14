package com.example.basic_3_recycleview

import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.appcompat.view.menu.ActionMenuItemView
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.item_main.view.*

class MainAdapter(val items: List<MainData>, val onItemClick: (Int)->Unit): RecyclerView.Adapter<MainAdapter.MainViewHolder>() {
    val TAG = javaClass.simpleName

    inner class MainViewHolder(itemView: View): RecyclerView.ViewHolder(itemView) {
        val tvTitle = itemView.tv_main_title        // title 데이터를 출력할 view의 참조
        val tvContent = itemView.tv_main_content    // content 데이터를 출력할 view의 참조

        init {
            itemView.setOnClickListener {
                val pos = adapterPosition       // 현재 ViewHolder가 몇 번째 index인지 알 수 있는 속성
                if (pos != RecyclerView.NO_POSITION) {
                    Log.d(TAG, "Item Clicked!! - $pos")
                    onItemClick(pos)
                }
            }
        }
    }

    // item 하나를 관리할 viewHolder 생성
    override fun onCreateViewHolder(parent: ViewGroup, p1: Int): MainViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_main, parent, false)
        return MainViewHolder(view)
    }

    // 데이터(item)의 개수 리턴
    override fun getItemCount(): Int = items.size

    override fun onBindViewHolder(holder: MainViewHolder, position: Int) {
        items[position].let{ item ->
            with(holder){       // with --> apply + let
                tvTitle.text = item.title
                tvContent.text = item.content
            }
        }
    }
}