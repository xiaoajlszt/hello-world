#include <cstdlib>
#include <dlfcn.h>
#include <stdio.h>
#include <wchar.h>
#include <string>
using namespace std;

#define __stdcall

int main()
{
    int (__stdcall*L_TMSAEng_setOption)(int lOpt, const void* pValue, unsigned long lDataSize);
    int (__stdcall*L_TMSAEng_initialize)(const wchar_t* wzConfigurationPath, void *pReserved);
	int (__stdcall*L_TMSAEng_getPatternVersion)(unsigned long* pMajorVer, unsigned long* pMinorVer, unsigned long* pVersionNum);
	
	int ret = 0;
	int iLogLevel = 0;
    string eng_path = "/opt/trend/ddei/lib/libtmsa.so";
	//string ptn_path = "/opt/trend/ddei/temp/au/sal/tmsa2.ptn";
	string ptn_path = "/opt/trend/ddei/lib/pattern/tmsa/tmsa2.ptn";

	void *handle = dlopen(eng_path.c_str(), RTLD_LAZY);
	if(handle == NULL)
	{
		printf("dlopen error!");
		exit(1);
	}

    const wchar_t* pwszLogPath = L"/opt/trend/ddei/log/tmsa.log";

    if((L_TMSAEng_setOption = (int(__stdcall*)(int, const void*, unsigned long))dlsym(handle, "TMSAEng_setOption")) == NULL)
    {
        exit(1);
    }

    ret = L_TMSAEng_setOption(1, pwszLogPath, wcslen(pwszLogPath) * sizeof(wchar_t));
    if(ret != 0)
    {
        printf("TMSAEng_setOption error!");
        exit(1);
    }
    else
    {
        printf("set log path ok!\n");
    }

    ret = L_TMSAEng_setOption(2, &iLogLevel, sizeof(iLogLevel));
    if (0 != ret)
    {
        printf("TMSAEng_setOption TM_SA_OPT_LOGLEVEL failed! Err: %d.", ret);
        exit(1);
    }

	if ((L_TMSAEng_initialize = (int(__stdcall*)(const wchar_t*, void*))dlsym(handle, "TMSAEng_initialize")) == NULL)
	{
		exit(1);
	}
	
	wchar_t  ws[256];
    swprintf(ws, 256, L"%hs", ptn_path.c_str());
    static const wstring PRODUCT_NAME = L"ddei";

	ret = L_TMSAEng_initialize(ws, (void *)PRODUCT_NAME.c_str());
	if(ret != 0)
	{
		printf("TMSAEng_initialize error! ret = %d", ret);
		exit(1);
	}

    if ((L_TMSAEng_getPatternVersion = (int(__stdcall*)(unsigned long*, unsigned long*, unsigned long*))dlsym(handle, "TMSAEng_getPatternVersion")) == NULL)
    {
        exit(1);
    }

    unsigned long MajorVer;
    unsigned long MinorVer;
    unsigned long BuildNum;

    ret = L_TMSAEng_getPatternVersion(&MajorVer, &MinorVer, &BuildNum);
    if(ret != 0)
    {
        printf("TMSAEng_getPatternVersion error!");
    }
    else
    {
        printf("%d.%d.%d", MajorVer, MinorVer, BuildNum);
    }
	
	exit(0);
}
