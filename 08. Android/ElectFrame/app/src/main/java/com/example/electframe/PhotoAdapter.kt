package com.example.electframe

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.appcompat.view.menu.ActionMenuItemView
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import kotlinx.android.synthetic.main.item_photo.view.*

class PhotoAdapter(val item: List<String>, val onItemClick:(Int)->Unit):
    RecyclerView.Adapter<PhotoAdapter.MainViewHolder>() {
    val TAG = javaClass.simpleName

    inner class MainViewHolder(itemView: View): RecyclerView.ViewHolder(itemView) {
        val imgThumb = itemView.imgThumb

        init {
            itemView.setOnClickListener {
                val pos = adapterPosition
                if (pos != RecyclerView.NO_POSITION) {
                    onItemClick(pos)
                }
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MainViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_photo,parent,false)
        return MainViewHolder(view)
    }

    override fun getItemCount() = items.size

    override fun onBindViewHolder(holder: MainViewHolder, position: Int) {
        items[position].let {
            with(holder){
                Glide.with(imgThumb)
                    .load(it)
                    .override(300,300)      // 이미지 크기 조정
                    .into(imgThumb)
            }
        }
    }
}