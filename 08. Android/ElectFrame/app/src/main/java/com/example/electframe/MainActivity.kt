package com.example.electframe

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.Manifest
import com.example.mylib.MediaImage
import com.example.mylib.PermissionChecker
import kotlinx.android.synthetic.main.activity_main.*
import org.jetbrains.anko.longToast
import kotlin.concurrent.timer


class MainActivity : AppCompatActivity() {
    val permissionChecker by lazy {
        val permissions =
            arrayOf(Manifest.permission.READ_EXTERNAL_STORAGE)
        PermissionChecker(this, permissions)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

//        val permissions = arrayOf(Manifest.permission.READ_EXTERNAL_STORAGE)
//        if (permissionChecker.check()) {
//            init()
//        }
        val pos = intent.getIntExtra(PhotoGridActivity.KEY_PHOTO_INDEX, 0)
        val mediaImage = MediaImage(this)

        val adapter = PhotoPagerAdapter(
            this,
            mediaImage.getAllPhotos()
        )
        viewPager.adapter = adapter
        viewPager.currentItem = pos
        // 3초마다 자동으로 슬라이드
        timer(period = 3000) {
            runOnUiThread {
                if (viewPager.currentItem < adapter.itemCount - 1) {
                    viewPager.currentItem++
                } else {
                    viewPager.currentItem = 0
                }
            }
        }
    }
}

//    override fun onRequestPermissionsResult(
//        requestCode: Int,
//        permissions: Array<out String>,
//        grantResults: IntArray
//    ) {
//        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
//        if (permissionChecker.checkGranted(requestCode, permissions, grantResults)) {
//            init()
//        } else {
//            // 권한 획득 실패
//            longToast("앱을 실행하려면 권한 승인이 필요합니다.")
//            finish()
//        }
//    }
//
//    private fun init() {
//        longToast("액티비티 초기화")
//
//        // 갤러리로부터 이미지 목록을 얻는 것
//        // photoPaterAdapter 생성
//        // Pager에 등록록
//
//        val megiaImage = MediaImage(this)
//        val adapter = PhotoPagerAdapter(this, megiaImage.getAllPhotos())
//        viewPager.adapter = adapter
//
//        // 3초마다 자동으로 슬라이드
//        timer(period = 3000) {
//            runOnUiThread {
//                if (viewPager.currentItem < adapter.itemCount-1){
//                    viewPager.currentItem ++
//                } else {
//                    viewPager.currentItem = 0
//                }
//            }
//        }
//    }
//  }

