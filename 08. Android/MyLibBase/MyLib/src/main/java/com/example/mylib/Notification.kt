package com.example.mylib

import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.ClipDescription
import android.content.Context
import android.content.Intent
import android.os.Build
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.NotificationCompat
import androidx.core.app.NotificationManagerCompat
import androidx.core.content.ContextCompat.startActivity

class Notification (val context: Context){
    fun createNotificationChannel(
            channelId: String,
            name: String,
            description: String,
            importance: Int = NotificationManager.IMPORTANCE_DEFAULT,
            showBadge: Boolean = false) {
        if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.O){
            val channel = NotificationChannel(channelId, name, importance)
            channel.setShowBadge(showBadge)
            channel.description = description
            val notificationManager = context.getSystemService(
                    NotificationManager::class.java
            )
            notificationManager.createNotificationChannel(channel)
        }
    }

    fun <T: AppCompatActivity>getPendingIntent(cls:Class<T>,
    requestCode: Int,
    flag:Int = PendingIntent.FLAG_CANCEL_CURRENT): PendingIntent{
        val intent = Intent(context, cls)
        intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or
                Intent.FLAG_ACTIVITY_CLEAR_TASK
        val pendingIntent = PendingIntent.getActivity(context, requestCode, intent, flag)
        return pendingIntent
    }

    fun notifyBasic(channelId:String, notification_id: Int, title:String, content:String, icon:Int, pendingIntent:PendingIntent){
        val builder = NotificationCompat.Builder(context,channelId).apply{
            setSmallIcon(icon)
            setContentTitle(title)
            setContentText(content)
            priority = NotificationCompat.PRIORITY_DEFAULT
            setAutoCancel(true)
            setContentIntent(pendingIntent)
        }
        val notificationManager = NotificationManagerCompat.from(context)
        notificationManager.notify(notification_id, builder.build())
    }
}