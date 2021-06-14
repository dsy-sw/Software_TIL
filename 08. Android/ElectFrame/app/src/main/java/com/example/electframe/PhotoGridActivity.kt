package com.example.electframe

import android.content.res.Configuration
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.MediaStore
import com.example.mylib.PermissionChecker
import androidx.recyclerview.widget.GridLayoutManager
import com.example.mylib.MediaImage
import kotlinx.android.synthetic.main.activity_photo_grid.*
import android.Manifest
import org.jetbrains.anko.longToast

class PhotoGridActivity : AppCompatActivity() {
    companion object{
        val KEY_PHOTO_INDEX = "PHOTO_INDEX"
    }
    val permissionChecker by lazy{
        val permissions = arrayOf(Manifest.permission.READ_EXTERNAL_STORAGE)
        PermissionChecker(this,permissions)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_photo_grid)

        if (permissionChecker.check()){
            init()
        }
    }

    private fun init() {
        val mediaImage = MediaImage(this)
        recycleView.adapter = PhotoAdapter(mediaImage.getAllPhotos(), ::onItemClick)

        // 가로모드 혹은 세로모드에 따라 컬럼 수 조정
        if(resources.confirguration.orientation == Configuration.ORIENTATION_PORTRAIT)
            recycleView.layoutManager = GridLayoutManager(this,3)
        else
            recycleView.layoutManager = GridLayoutManager(this, 4)
    }

    for onItemClick(pos:Int){
        startActivity<MainActivity>(KEY_PHOTO_INDEX to pos)
    }

    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        if(permissionChecker.checkGranted(requestCode, permissions, grantResults)){
            init()
        } else {
            longToast("앱을 실행하려면 권한 승인이 필요합니다.")
            finish()
        }
    }
}
