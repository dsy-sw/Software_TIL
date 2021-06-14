package com.example.mylib.openapi.openweather

import android.util.Log
import com.example.mylib.openapi.OpenApi
import com.example.mylib.openapi.kakao.image.data.ImageSearchResult
import com.example.mylib.openapi.openweather.data.WeatherCast
import com.example.mylib.openapi.piapi.PiApi
import com.example.mylib.openapi.piapi.PiApiService
import com.example.mylib.openapi.piapi.data.ControlResult
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET
import retrofit2.http.Query

const val API_KEY="e21a1f5002a50f1e16292431128b9ca8"

interface OpenWeatherService {
    // http://api.openweathermap.org/data/2.5/weather?q=Seoul&APPID=93ec9acd67f5e6d7fd08ff43c857eeac&lang=kr
    @GET("/data/2.5/weather")
    fun qetWeatherCast( // Call 객체를 만드는 factory method
        @Query("q") city: String,
        @Query("APPID") apiKey: String = API_KEY,
        @Query("lang") lang: String = "kr"
    ): Call<WeatherCast>  // 실제 호출하는 객체를 리턴
}


object OpenWeather : OpenApi(){
    override val TAG = javaClass.simpleName
    override val BASE_URL = "http://211.214.228.114:8000"

    private val service = retrofit.create(OpenWeatherService::class.java)

    fun qetWeatherCast(city: String, callback: (WeatherCast)->Unit) {
        service.qetWeatherCast(city)
            .enqueue(ApiCallback<WeatherCast>(callback))
    }
}


//    object OpenWeather {
//        val TAG = javaClass.simpleName
//        private val retrofit = Retrofit.Builder()
//            .baseUrl("http://api.openweathermap.org")
//            .addConverterFactory(GsonConverterFactory.create())
//            .build()
//
//        fun getService(): OpenWeatherService = retrofit.create(
//            OpenWeatherService::class.java
//        )
//
//        fun qetWeatherCast(city: String, callback: (WeatherCast) -> Unit) {
//            getService()
//                .qetWeatherCast(city)
//                .enqueue(object : Callback<WeatherCast> {
//                    override fun onFailure(call: Call<WeatherCast>, t: Throwable) {
//                        Log.e(TAG, t.toString())
//                    }
//
//                    override fun onResponse(
//                        call: Call<WeatherCast>,
//                        response: Response<WeatherCast>
//                    ) {
//                        if (response.isSuccessful) { // code : 200 체크
//                            val result = response.body()    // body()의 리턴 타입 ImageSearchResult?
//                            callback(result!!)
//                        } else {
//                            Log.w(TAG, "${response.code()}, ${response.message()}")
//                            Log.w(TAG, "${response.toString()}")
//                        }
//                    }
//                })
//        }
//    }
//}