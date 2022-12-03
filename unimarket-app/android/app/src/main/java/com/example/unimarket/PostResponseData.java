package com.example.unimarket;

import com.google.gson.annotations.SerializedName;

public class PostResponseData {

    @SerializedName("title")
    private String title;

    @SerializedName("picture")
    private String picture;

    @SerializedName("region")
    private String region;

    @SerializedName("price")
    private int price;

    @SerializedName("link")
    private String link;

    @SerializedName("app_name")
    private String app_name;

    public PostResponseData(String title, String picture, String region, int price, String link, String app_name) {
        this.title = title;
        this.picture = picture;
        this.region = region;
        this.price = price;
        this.link = link;
        this.app_name = app_name;
    }
}
