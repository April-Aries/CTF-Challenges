# Dear Diary

| Information | Description |
| :-- | :-- |
| Category | Forensics |
| Difficulty | Medium |

:label: **autopsy**

# 題目敘述

If you can find the flag on this disk image, we can close the case for good! Download the disk image [here](https://artifacts.picoctf.net/c_titan/63/disk.flag.img.gz).

> Hint: If you're observing binary data raw in the terminal you may be misled about the contents of a block.

# 解題過程

1. 這題給了一個 image 檔 `disk.flag.img.gz`. 先透過 `gunzip disk.flag.img.gz` 指令將它解壓縮
2. 這題會用到一個工具叫做 `autopsy` 來分析硬碟來分析硬碟檔。直接在 terminal 打上 `autopsy`，它會給一個 URL，把這個 URL 打開就會試等等工具的使用介面（以這題來說就是 http://localhost:9999/autopsy）
    ![image](https://hackmd.io/_uploads/BJrdBUku1e.png)
3. 在正式開始分析之前有一系列步驟要先完成，可以想成要先建一個專案資料夾放等等要用到的東西、這次分析的基本資訊等等
    - 首先是創建一個 case，點選 **New Case**，填寫 case 名稱 (**Case Name**)，說明 (Description) 和研究者 (Investigator names) 可不填
        ![image](https://hackmd.io/_uploads/ry5BjIJOJl.png)
        ![image](https://hackmd.io/_uploads/S1sri8ydkx.png)
    - 接著要新增該 case 的主機，點擊 **Add Host** 並填寫 Host 名稱 (**Host Name**)，其他欄位一樣是選填，按照預設過去就可以了
        ![image](https://hackmd.io/_uploads/ry2AwIkOyx.png)
        ![image](https://hackmd.io/_uploads/BylyYUkd1l.png)
    - 再來就是匯入 image 檔，點選 **Add Image** > **Add Image File** 匯入硬碟檔，硬碟檔位置 (**Location**) 記得要填寫絕對位置，其他一樣維持預設值即可，
        ![image](https://hackmd.io/_uploads/Skq4t8y_yl.png)
        ![image](https://hackmd.io/_uploads/ByJYY8k_1g.png)
        ![image](https://hackmd.io/_uploads/rkv3cL1dyg.png)
        ![image](https://hackmd.io/_uploads/BkbSsLJdye.png)
4. 分析直接點擊 **Analyze**，因為要猜 flag，所以選擇 **Keyword Search**
    ![image](https://hackmd.io/_uploads/B1iFoUJuyx.png)
    ![image](https://hackmd.io/_uploads/SkMnsUJd1x.png)
5. 策略是 flag 的長相為 `pico{XXX}`，所以先來猜會不會有 `pico` 字串的檔案
    ![image](https://hackmd.io/_uploads/SkcEhIydkg.png)
    好吧！很可惜沒有
6. 下一個策略是 flag 可能會是一個 txt 檔，那搜尋 `.txt` 試試看
    ![image](https://hackmd.io/_uploads/BJx8aUydyg.png)
    ![image](https://hackmd.io/_uploads/rJeLpIJ_1g.png)
    ![image](https://hackmd.io/_uploads/r1ZIaU1_kl.png)
    ![image](https://hackmd.io/_uploads/Hk-LaUJ_ke.png)
    ![image](https://hackmd.io/_uploads/Bk-868ydyx.png)
    ![image](https://hackmd.io/_uploads/SyWU6Ikdyl.png)
    ![image](https://hackmd.io/_uploads/HkZUa8Jukg.png)
    ![image](https://hackmd.io/_uploads/Bk-Lp81dkx.png)
    ![image](https://hackmd.io/_uploads/HJb8aI1d1x.png)
    ![image](https://hackmd.io/_uploads/SybIaL1dye.png)
    仔細觀察其中一段檔案會發現每一個檔案都包含 flag 的一部分，組成起來就是完整的 flag 了

- :triangular_flag_on_post:: `picoCTF{1_533_n4m35_80d24b30}`

# 註記

1. 如果發現輸入 `autopsy` 無法執行並得到 *"can't open log: autopsy.log at /usr/share/autopsy/lib/print.pm line 383."* 的 error message，就換成 `sudo autopsy` 執行
2. 這題沒特別放 image file，因為檔案太大了

# 參考資料

- [picoCTF 2024: Dear Diary](https://medium.com/@niceselol/picoctf-2024-dear-diary-f7eafbc389ea)
- [picoCTF 2024 — Write-up — Forensics](https://infosecwriteups.com/picoctf-2024-write-up-forensics-c471e79e6af9#4cfa)
- [Can't open log: autopsy.log at /usr/share/autopsy/lib/Print.pm line 383. #6126](https://github.com/sleuthkit/autopsy/issues/6126)
