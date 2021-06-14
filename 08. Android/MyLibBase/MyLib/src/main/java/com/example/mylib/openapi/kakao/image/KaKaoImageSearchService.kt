package com.example.mylib.openapi.kakao.image

import android.util.Log
import com.example.mylib.openapi.kakao.image.data.ImageSearchResult
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET
import retrofit2.http.Headers
import retrofit2.http.Query


interface KaKaoImageSearchService {

    @Headers("Authorization: KakaoAK bc68209ded22c26bb3c2e80894ca0a14")
    @GET("/v2/search/image")
    fun requestSearchImage(     // call 객체를 만드는 factory method
        @Query("query") keyword: String,
        @Query("sort") sort: String = "recency",
        @Query("page") page: Int,
        @Query("size") size: Int = 10
    ): Call<ImageSearchResult>      // 실제 호출하는 객체
}

// signleton : 오직 한 개의 인스턴스만 운영
// 자동으로 인스턴스가 만들어짐

object KakaoImageSearch {
    private val retrofit = Retrofit.Builder()
        .baseUrl("https://dapi.kakao.com")
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    fun getService() : KaKaoImageSearchService =
        retrofit.create(
            KaKaoImageSearchService::class.java)

    fun searchImage(keyword: String, page: Int, callback: (ImageSearchResult)->Unit) {
        getService()
            .requestSearchImage(keyword = keyword, page = page)
            .enqueue(object: Callback<ImageSearchResult> {
                override fun onFailure(call: Call<ImageSearchResult>, t: Throwable) {
                    Log.e("----", t.toString())
                }

                override fun onResponse(
                    call: Call<ImageSearchResult>,
                    response: Response<ImageSearchResult>
                ) {
                    if(response.isSuccessful) {     // code : 200 체크
                        val result = response.body()    //body()의 리턴 타입 ImageSearchResult?
                        Log.i("MainActivity", result.toString())
                        callback(result!!)
                    }else{
                        Log.w("MainAvctivity", "${response.code()}, ${response.message()}")     // 실패 시 해당 오류의 code, message 출력
                        Log.w("MainAvctivity", "${response.toString()}")                        // 실패 시 오류 문자열 출력
                    }
                }
            })
    }
}