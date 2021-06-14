package com.example.basic_2_activitylife

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.PersistableBundle
import android.util.Log

class MainActivity : AppCompatActivity() {
    val TAG = javaClass.simpleName
    var nLineNumber = 0
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        Log.d(TAG, "${nLineNumber++}: OnCreate")
    }

    override fun onStart() {
        super.onStart()
        Log.d(TAG, "${nLineNumber++}: OnStart")

    }

    override fun onResume() {
        super.onResume()
        Log.d(TAG, "${nLineNumber++}: OnResume")
    }

    override fun onPause() {
        super.onPause()
        Log.d(TAG, "${nLineNumber++}: OnPause")
    }

    override fun onStop() {
        super.onStop()
        Log.d(TAG, "${nLineNumber++}: OnStop")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d(TAG, "${nLineNumber++}: OnDestroy")
    }
}